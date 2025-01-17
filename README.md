# CoinTracking Integration for Home Assistant

This integration allows you to connect your CoinTracking account to Home Assistant, enabling you to track your account balance and other metrics directly from the Home Assistant dashboard.

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
   git clone https://github.com/your-repo/home-assistant-cointracking
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

4. **Update your configuration.yaml:**
   Add the following:
   ```yaml
   sensor:
     - platform: cointracking
       api_key: YOUR_API_KEY
       api_secret: YOUR_API_SECRET
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

## License

This project is licensed under the [MIT License](LICENSE).

### Original Creator
This integration was inspired by and builds upon the work of [ChristophCaina](https://gist.github.com/ChristophCaina). Special thanks for the groundwork provided.

---

## Support
For issues or feature requests, please visit the [issue tracker](https://github.com/your-repo/issues).

---

Enjoy tracking your crypto assets with Home Assistant!
