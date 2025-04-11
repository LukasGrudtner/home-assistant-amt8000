
DOMAIN = "amt8000"

from .zone_coordinator import Amt8000ZoneCoordinator

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass, config_entry):
    host = config_entry.data["host"]
    port = config_entry.data["port"]
    password = config_entry.data["password"]

    coordinator = Amt8000ZoneCoordinator(hass, host, port, password)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[config_entry.entry_id] = {
        "host": host,
        "port": port,
        "password": password,
        "coordinator": coordinator
    }

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "binary_sensor")
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "alarm_control_panel")
    )

    return True

async def async_unload_entry(hass, config_entry):
    return True
