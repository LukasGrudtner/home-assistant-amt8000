
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    await coordinator.async_config_entry_first_refresh()

    entities = []
    for zone_id in coordinator.data:
        entities.append(Amt8000ZoneSensor(hass, coordinator, zone_id))

    async_add_entities(entities)

class Amt8000ZoneSensor(CoordinatorEntity, BinarySensorEntity):
    def __init__(self, hass, coordinator, zone_id):
        super().__init__(coordinator)
        self.hass = hass
        self._attr_name = f"Zona {zone_id}"
        self._attr_unique_id = f"amt8000_zone_{zone_id}"
        self.zone_id = zone_id
        self._previous_state = None

    @property
    def is_on(self):
        return self.coordinator.data.get(self.zone_id, False)

    async def async_update(self):
        await self.coordinator.async_request_refresh()
        current = self.coordinator.data.get(self.zone_id, False)

        if self._previous_state is not None and current != self._previous_state:
            self.hass.bus.async_fire(
                "amt8000.zone_triggered",
                {
                    "zone": self.zone_id,
                    "state": "on" if current else "off"
                }
            )

        self._previous_state = current
