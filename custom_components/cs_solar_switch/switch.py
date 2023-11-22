import logging
import requests
from homeassistant.helpers.entity import ToggleEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
#API_URL = "https://api.connect-smart.nl/cs_solar_switch"
API_URL = "https://www.voxip.nl/api/"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the CS Solar Switch."""
    async_add_entities([CSSolarSwitch()])


class CSSolarSwitch(ToggleEntity):
    """Representation of a CS Solar Switch."""

    def __init__(self):
        """Initialize the switch."""
        self._state = False

    @property
    def name(self):
        """Return the name of the switch."""
        return "CS Solar Switch"

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        # Implement logic to update the switch state from the external API
        self._update_state()
        self.schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        # Implement logic to update the switch state from the external API
        self._update_state()
        self.schedule_update_ha_state()

    def _update_state(self):
        """Update the state from the external API."""
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
            self._state = data["switch_state"]
        except requests.exceptions.RequestException as err:
            _LOGGER.error(f"Error updating state: {err}")
            self._state = False  # Set to False in case of an error
