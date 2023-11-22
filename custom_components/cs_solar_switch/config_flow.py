"""Config flow for CS Solar Switch."""
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_USERNAME

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class CSSolarSwitchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CS Solar Switch."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Validate the entered credentials if needed
            # If validation fails, return {"errors": {"base": "invalid_credentials"}}
            # Otherwise, return self.async_create_entry(title="CS Solar Switch", data=user_input)
            return self.async_create_entry(title="CS Solar Switch", data={})

        return self._show_config_form()

    def _show_config_form(self, errors=None):
        """Show the configuration form."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(CONF_USERNAME): str}),
            errors=errors,
        )
