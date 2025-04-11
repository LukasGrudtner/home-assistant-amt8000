
import asyncio
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

class Amt8000ZoneCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, host, port):
        super().__init__(hass, _LOGGER, name="amt8000_zones")
        self.host = host
        self.port = port
        self.zones = {}

    async def _async_update_data(self):
        try:
            reader, writer = await asyncio.open_connection(self.host, self.port)
            writer.write(b"\xE9\x21\x31\x32\x33\x34\x5A\x21")  # comando de status
            await writer.drain()
            raw = await reader.read(256)
            writer.close()
            await writer.wait_closed()

            # Simulação: vamos supor que os primeiros 8 bytes representam 8 zonas
            self.zones = {f"Z{str(i+1).zfill(2)}": raw[i] == 0x01 for i in range(8)}
            return self.zones

        except Exception as e:
            _LOGGER.error("Erro ao atualizar zonas: %s", e)
            raise
