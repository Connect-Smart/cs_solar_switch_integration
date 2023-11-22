import logging
from homeassistant.helpers.entity import ToggleEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the CS Solar Switch."""
    async_add_entities([CssolarSwitch()])


class CssolarSwitch(ToggleEntity):
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
        self._state = True
        self.schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        self._state = False
        self.schedule_update_ha_state()
