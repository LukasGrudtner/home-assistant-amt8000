
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class Amt8000OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        zone_names = self.config_entry.options.get("zone_names", {})

        if user_input is not None:
            return self.async_create_entry(title="", data={"zone_names": user_input})

        schema = vol.Schema({
            vol.Optional("Z01", default=zone_names.get("Z01", "Zona Z01")): str,
            vol.Optional("Z02", default=zone_names.get("Z02", "Zona Z02")): str,
            vol.Optional("Z03", default=zone_names.get("Z03", "Zona Z03")): str,
            vol.Optional("Z04", default=zone_names.get("Z04", "Zona Z04")): str,
            vol.Optional("Z05", default=zone_names.get("Z05", "Zona Z05")): str,
            vol.Optional("Z06", default=zone_names.get("Z06", "Zona Z06")): str,
            vol.Optional("Z07", default=zone_names.get("Z07", "Zona Z07")): str,
            vol.Optional("Z08", default=zone_names.get("Z08", "Zona Z08")): str,
        })

        return self.async_show_form(step_id="init", data_schema=schema)

@callback
def async_get_options_flow(config_entry):
    return Amt8000OptionsFlowHandler(config_entry)
