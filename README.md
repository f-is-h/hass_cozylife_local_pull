# CozyLife & Home Assistant (Updated for Home Assistant 2025.5+)

CozyLife Assistant integration is developed for controlling CozyLife devices using local net. This is an updated version compatible with Home Assistant 2025.5 and later versions.

**Original repository:** https://github.com/cozylife/hass_cozylife_local_pull  
**Updated by:** @f-is-h

## What's Changed in This Version

- **Fixed Home Assistant 2025.5+ compatibility:** Resolved the `'HomeAssistant' object has no attribute 'helpers'` error
- **Modernized API usage:** Updated from deprecated `hass.helpers.discovery.load_platform` to modern async platform loading
- **Improved error handling:** Better logging and exception handling
- **Async support:** All platform functions are now properly async
- **Code cleanup:** Updated to modern Python patterns and Home Assistant best practices

## Supported Device Types

- RGBCW Light
- CW Light  
- Switch & Plug

## Install

* A home assistant environment that can access the external network
* Download or clone this updated repo to the custom_components directory
* Configuration in configuration.yaml:

```yaml
hass_cozylife_local_pull:
   lang: en
   ip:
     - "192.168.1.99"
```

## Changes from Original

### Fixed Issues:
- ✅ `'HomeAssistant' object has no attribute 'helpers'` error
- ✅ Deprecated `hass.helpers.discovery.load_platform` usage
- ✅ Synchronous setup functions replaced with async versions
- ✅ Improved platform loading mechanism
- ✅ Better error handling and logging

### Technical Improvements:
- Modern async/await patterns
- Updated manifest.json with proper metadata
- Cleaner code structure following Home Assistant guidelines
- Better type hints and documentation

## Compatibility

- **Home Assistant:** 2025.5+
- **Python:** 3.11+

## Feedback

* Please submit an issue to this repository
* For original CozyLife support: Send an email with the subject of hass support to info@cozylife.app

## Troubleshoot 

* Check whether the internal network isolation of the router is enabled
* Check if the plugin is in the right place
* Restart Home Assistant multiple times
* View the output log of the plugin
* Ensure you're using Home Assistant 2025.5 or later

## TODO

- Sending broadcasts regularly has reached the ability to discover devices at any time
- Support sensor device
- Consider adding Config Flow for modern setup experience

## PROGRESS

- ✅ Fixed Home Assistant 2025.5+ compatibility
- ✅ Modernized platform loading
- ✅ Improved async support
- ✅ Enhanced error handling
