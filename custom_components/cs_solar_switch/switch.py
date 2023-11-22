"""
Custom component to integrate cs_solar_switch with Home Assistant.
"""
import logging
import requests
import voluptuous as vol
from homeassistant.const import CONF_API_KEY
from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "cs_solar_switch"
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    api_key = config.get(CONF_API_KEY)
    add_entities([CsSolarSwitch(api_key)], True)

class CsSolarSwitch(SwitchEntity):
    def __init__(self, api_key):
        self._api_key = api_key
        self._state = False

    @property
    def name(self):
        return "Cs Solar Switch"

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._state = True

    def turn_off(self, **kwargs):
        self._state = False

    def update(self):
        try:
            # Make API request to https://voxip.nl/api and update switch state
            response = requests.get("https://voxip.nl/api", headers={"Authorization": f"Bearer {self._api_key}"})
            data = response.json()

            # Check if the API response is True and update the switch state accordingly
            if data.get("result") == True:
                self._state = True
            else:
                self._state = False

        except Exception as e:
            _LOGGER.error(f"Error updating cs_solar_switch: {e}")
