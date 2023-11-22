"""Config flow for Cs Solar Switch integration."""
from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

DOMAIN = "cs_solar_switch"

async def async_setup(hass, config):
    return True

class CsSolarSwitchFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="Cs Solar Switch",
                data={},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=config_entries.HANDLER_SCHEMA,
        )

config_entry_flow.register_discovery_flow(
    DOMAIN,
    "Cs Solar Switch",
    CsSolarSwitchFlowHandler,
)
