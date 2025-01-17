# CoinTracking Integration for Home Assistant

This integration allows you to connect your CoinTracking account to Home Assistant, enabling you to track your account balance and other metrics directly from the Home Assistant dashboard.

I stopped finishing this integration because API access is pay walled. I cannot test if the integration works behind the pay-wall.

## Features
- Fetches real-time account balance data from CoinTracking.info.
- Displays balance in USD or your preferred currency.
- Supports Home Assistant's sensor platform.

---

## Installation

### Manual Installation

1. **Download the repository files:**
   - Clone this repository or download the ZIP file.

   ```bash
   git clone https://github.com/RoyOltmans/cointrackinginfo
   ```

2. **Copy the component:**
   - Move the `cointracking` directory to your Home Assistant `custom_components` folder.
     ```
     .homeassistant/
     ├── custom_components/
     │   ├── cointracking/
     │       ├── __init__.py
     │       ├── sensor.py
     │       ├── manifest.json
     │       ├── hacs.json
     ```

3. **Restart Home Assistant:**
   - Go to **Settings** > **System** > **Restart** or restart the Home Assistant service manually.

3.1 **Fetch API keys at contracking.info**

Go to [API activation](https://cointracking.info/api/api.php) on cointracking and create the secret and the key (do not forget to copy them, the secret appears once) and add these to your secrets.yaml

3.2 **Update secrets.yaml**

How to use secrets see [manual home assistant](https://www.home-assistant.io/docs/configuration/secrets/)

Add the following:
```
contracking_api_key: "1234567890"
contracking_api_secret: "1234567890"
```

4. **Update your configuration.yaml:**
   Add the following:
   ```yaml
   sensor:
     - platform: cointracking
       api_key: !secret contracking_api_key
       api_secret: !secret contracking_api_secret
   ```

5. **Restart Home Assistant again:**
   - Apply the configuration changes.

---

## Configuration

| Key         | Required | Description                                      |
|-------------|----------|--------------------------------------------------|
| `api_key`   | Yes      | Your API key from CoinTracking.info             |
| `api_secret`| Yes      | Your API secret from CoinTracking.info          |

### Example Configuration
```yaml
sensor:
  - platform: cointracking
    api_key: "abcd1234"
    api_secret: "efgh5678"
```

---

## Disclaimer

**Use this tool at your own risk.**

- The authors and contributors of this project are not responsible for any damage, data loss, or issues caused by using this software.

## License

This project is licensed under the [MIT License](LICENSE).

### Original Creator
This integration was inspired by and builds upon the work of [ChristophCaina](https://gist.github.com/ChristophCaina). Special thanks for the groundwork provided.

---

## Support
For issues or feature requests, please visit the [issue tracker](https://github.com/RoyOltmans/cointrackinginfo).

---

Enjoy tracking your crypto assets with Home Assistant!
