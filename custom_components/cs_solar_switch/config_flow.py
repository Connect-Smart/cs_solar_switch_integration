"""Config flow for Cs Solar Switch integration."""
from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

DOMAIN = "cs_solar_switch"

async def async_setup(hass, config):
    return True

config_entry_flow.register_discovery_flow(
    DOMAIN,
    "Cs Solar Switch",
    lambda _: config_entries.ConfigEntry(
        version=1,
        domain=DOMAIN,
        title="Cs Solar Switch",
        data={},
    ),
)
