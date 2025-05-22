# CozyLife & Home Assistant (Updated for Home Assistant 2025.5+)

CozyLife Assistant integration is developed for controlling CozyLife devices using local net. This is an updated version compatible with Home Assistant 2025.5 and later versions.

**Original repository:** https://github.com/cozylife/hass_cozylife_local_pull  
**Updated by:** @f-is-h

## What's Changed in This Version

- ✅ **Fixed Home Assistant 2025.5+ compatibility:** Resolved the `'HomeAssistant' object has no attribute 'helpers'` error
- ✅ **Modernized API usage:** Updated from deprecated `hass.helpers.discovery.load_platform` to modern async platform loading
- ✅ **Improved repository structure:** Files now in root directory for easier installation (clone and use!)
- ✅ **Enhanced error handling:** Better logging and exception handling
- ✅ **Async support:** All platform functions are now properly async
- ✅ **Code cleanup:** Updated to modern Python patterns and Home Assistant best practices

## Supported Device Types

- RGBCW Light
- CW Light  
- Switch & Plug

## 🚀 Easy Installation

### Method 1: Direct Clone (Recommended)
```bash
cd /config/custom_components/
git clone https://github.com/f-is-h/hass_cozylife_local_pull.git
```
**That's it!** No extra steps needed. 

### Method 2: Manual Download
1. Download: https://github.com/f-is-h/hass_cozylife_local_pull/archive/refs/heads/main.zip
2. Extract to `/config/custom_components/hass_cozylife_local_pull/`

## Configuration

Add to your `configuration.yaml`:
```yaml
hass_cozylife_local_pull:
  lang: en
  ip:
    - "192.168.1.99"
    - "192.168.1.100"
```

## After Installation

1. **Restart Home Assistant**
2. Your devices should appear automatically
3. No more errors in logs!

## 🆚 Differences from Original Repository

### Repository Structure
**Original Issue:** The original repository had a nested structure that caused installation problems:
```
repo/custom_components/hass_cozylife_local_pull/  ← Files here
```
When cloned to `/config/custom_components/`, this created:
```
/config/custom_components/hass_cozylife_local_pull/custom_components/hass_cozylife_local_pull/
```
Home Assistant couldn't find the integration due to the extra nesting.

**Our Solution:** Component files are now directly in the root directory:
```
repo/  ← Files directly here
├── __init__.py
├── light.py
├── switch.py
└── ...
```
This follows Home Assistant community standards and enables "clone and use" installation.

### Installation Comparison

| Original Repository | Our Fixed Repository |
|:------------------:|:-------------------:|
| ❌ Clone → Manual file moving | ✅ Clone → Ready to use |
| ❌ Confusing nested paths | ✅ Standard structure |
| ❌ Easy to mess up | ✅ Foolproof installation |

## Changes from Original

### Fixed Issues:
- ✅ `'HomeAssistant' object has no attribute 'helpers'` error
- ✅ Deprecated `hass.helpers.discovery.load_platform` usage
- ✅ Synchronous setup functions replaced with async versions
- ✅ Improved platform loading mechanism
- ✅ Better error handling and logging
- ✅ Installation path confusion resolved

### Technical Improvements:
- Modern async/await patterns
- Updated manifest.json with proper metadata
- Cleaner code structure following Home Assistant guidelines
- Better type hints and documentation
- Repository structure optimized for easy installation

## Compatibility

- **Home Assistant:** 2025.5+
- **Python:** 3.11+
- **Backward compatible** with earlier HA versions

## Troubleshooting

### If you have the old version installed:
```bash
cd /config/custom_components/
rm -rf hass_cozylife_local_pull/
git clone https://github.com/f-is-h/hass_cozylife_local_pull.git
```

### Common issues:
- **No devices appear**: Check that devices are on the same network and ports 5555 (TCP) and 6095 (UDP) are not blocked
- **"Integration not found"**: Ensure files are in `/config/custom_components/hass_cozylife_local_pull/` (not nested)
- **Old errors persist**: Restart Home Assistant after installation

## Development & Testing

For developers and advanced users:

### Test Network Connectivity
```bash
cd /config/custom_components/hass_cozylife_local_pull/
python3 test_discovery.py
```

### Enable Debug Logging
Add to `configuration.yaml`:
```yaml
logger:
  default: info
  logs:
    custom_components.hass_cozylife_local_pull: debug
```

## Feedback & Support

- **Issues with this version**: [Create an issue](https://github.com/f-is-h/hass_cozylife_local_pull/issues)
- **Original CozyLife support**: info@cozylife.app

## Contributing

Feel free to submit issues and pull requests. This repository aims to maintain compatibility with the latest Home Assistant versions while preserving all original functionality.

---

**⭐ If this helped you, please star the repository to help others find the fix!**