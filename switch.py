"""Platform for switch integration."""
from __future__ import annotations

import logging
from typing import Any
import time

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import (
    DOMAIN,
    SWITCH_TYPE_CODE,
    LIGHT_TYPE_CODE,
    LIGHT_DPID,
    SWITCH,
    WORK_MODE,
    TEMP,
    BRIGHT,
    HUE,
    SAT,
)
from .tcp_client import tcp_client

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the switch platform via YAML discovery."""
    _LOGGER.debug("Setting up switch platform")
    
    if discovery_info is None:
        return

    domain_data = hass.data.get(DOMAIN, {})
    tcp_clients = domain_data.get('tcp_client', [])
    
    switches = []
    for client in tcp_clients:
        if SWITCH_TYPE_CODE == client.device_type_code:
            switches.append(CozyLifeSwitch(client))
    
    async_add_entities(switches)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform via config entry."""
    domain_data = hass.data[DOMAIN][entry.entry_id]
    tcp_clients = domain_data.get('tcp_client', [])
    
    switches = []
    for client in tcp_clients:
        if SWITCH_TYPE_CODE == client.device_type_code:
            switches.append(CozyLifeSwitch(client))
    
    async_add_entities(switches)


class CozyLifeSwitch(SwitchEntity):
    """Representation of a CozyLife Switch."""
    
    def __init__(self, tcp_client: tcp_client) -> None:
        """Initialize the switch."""
        _LOGGER.debug("Initializing CozyLife Switch")
        self._tcp_client = tcp_client
        self._attr_unique_id = tcp_client.device_id
        self._attr_name = f"{tcp_client.device_model_name} {tcp_client.device_id[-4:]}"
        self._state = {}
        self._attr_is_on = False
        self._available = False
        self._last_update = 0
        self._update_interval = 30  # 30秒更新间隔，避免频繁查询
        self._refresh_state()
    
    def _refresh_state(self) -> None:
        """Query device and update state."""
        try:
            # 限制查询频率
            current_time = time.time()
            if current_time - self._last_update < self._update_interval:
                return
                
            self._state = self._tcp_client.query()
            self._last_update = current_time
            
            # 检查状态数据是否有效
            if self._state and isinstance(self._state, dict) and '1' in self._state:
                self._attr_is_on = self._state.get('1', 0) != 0
                self._available = True
                _LOGGER.debug("Switch state refreshed successfully: %s", self._attr_is_on)
            else:
                # 如果获取状态失败，保持之前的状态，但标记为不可用
                self._available = False
                _LOGGER.warning("Failed to get valid state from device, marking as unavailable")
                
        except Exception as err:
            self._available = False
            _LOGGER.error("Error refreshing switch state: %s", err)
    
    @property
    def available(self) -> bool:
        """Return if the device is available."""
        return self._available
    
    @property
    def is_on(self) -> bool:
        """Return True if entity is on."""
        # 只在必要时刷新状态
        self._refresh_state()
        return self._attr_is_on
    
    async def async_update(self) -> None:
        """Update the entity state."""
        await self.hass.async_add_executor_job(self._refresh_state)
    
    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        _LOGGER.debug("Turning on switch with kwargs: %s", kwargs)
        
        try:
            success = self._tcp_client.control({'1': 255})
            if success:
                self._attr_is_on = True
                self._available = True
                # 控制成功后强制刷新状态
                self._last_update = 0
                await self.hass.async_add_executor_job(self._refresh_state)
            else:
                _LOGGER.error("Failed to turn on switch")
                self._available = False
        except Exception as err:
            _LOGGER.error("Error turning on switch: %s", err)
            self._available = False
    
    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        _LOGGER.debug("Turning off switch")
        
        try:
            success = self._tcp_client.control({'1': 0})
            if success:
                self._attr_is_on = False
                self._available = True
                # 控制成功后强制刷新状态
                self._last_update = 0
                await self.hass.async_add_executor_job(self._refresh_state)
            else:
                _LOGGER.error("Failed to turn off switch")
                self._available = False
        except Exception as err:
            _LOGGER.error("Error turning off switch: %s", err)
            self._available = False