from datetime import timedelta
import logging
import hmac
import time
from hashlib import sha512
from urllib.parse import urlencode
import requests

from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_SCAN_INTERVAL,
    STATE_UNKNOWN,
    ATTR_ATTRIBUTION,
)
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "cointracking"

CONF_API_KEY = "api_key"
CONF_API_SECRET = "api_secret"

DEFAULT_NAME = "CoinTracking Balance"
DEFAULT_SCAN_INTERVAL = timedelta(minutes=15)

ICON = "mdi:currency-usd"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_API_SECRET): cv.string,
        vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): cv.time_period,
    }
)

COINTRACKING_API_URL = "https://cointracking.info/api/v1/"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the CoinTracking sensor platform."""
    api_key = config[CONF_API_KEY]
    api_secret = config[CONF_API_SECRET]
    scan_interval = config.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    async_add_entities([CoinTrackingSensor(api_key, api_secret)], True)


class CoinTrackingSensor(Entity):
    """Representation of a CoinTracking sensor."""

    def __init__(self, api_key, api_secret):
        """Initialize the sensor."""
        self._api_key = api_key
        self._api_secret = api_secret
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        """Return the name of the sensor."""
        return "CoinTracking Balance"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    @property
    def icon(self):
        """Icon to use in the frontend."""
        return ICON

    def update(self):
        """Fetch the latest balance data."""
        nonce = int(time.time())
        params = {"method": "getBalance", "nonce": nonce}
        encoded_params = urlencode(params)
        message = encoded_params.encode("utf-8")
        secret = self._api_secret.encode("utf-8")
        signature = hmac.new(secret, message, sha512).hexdigest()

        headers = {"Key": self._api_key, "Sign": signature}
        response = requests.post(COINTRACKING_API_URL, data=params, headers=headers, timeout=10)

        if response.status_code != 200:
            _LOGGER.error(f"Error fetching CoinTracking data: {response.status_code}")
            self._state = STATE_UNKNOWN
            return

        try:
            data = response.json()
            _LOGGER.debug(f"CoinTracking API response: {data}")  # Log full API response

            if "error" in data:
                _LOGGER.error(f"API Error: {data['error']}")
                self._state = STATE_UNKNOWN
                return

            balance = data["summary"]["value_fiat"]
            self._state = round(float(balance), 2)
            self._attributes = {"currency": "USD"}
        except (KeyError, ValueError) as error:
            _LOGGER.error(f"Error processing CoinTracking response: {error}")
            self._state = STATE_UNKNOWN
