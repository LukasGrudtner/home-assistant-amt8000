from homeassistant.components.binary_sensor import BinarySensorEntity

class Amt8000ZoneSensor(BinarySensorEntity):
    def __init__(self, name, zone_id, panel):
        self._attr_name = name
        self._zone_id = zone_id
        self._state = False
        self._panel = panel

    @property
    def is_on(self):
        return self._state

    async def async_update(self):
        command = self._panel.build_command(status_request=True)
        await self._panel.send_command(command)

    async def async_added_to_hass(self):
        await self.async_update()
