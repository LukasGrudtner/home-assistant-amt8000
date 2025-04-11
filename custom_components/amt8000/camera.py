from homeassistant.components.camera import Camera
import asyncio
import logging

_LOGGER = logging.getLogger(__name__)

class Amt8000Camera(Camera):
    def __init__(self, name, host, port):
        super().__init__()
        self._attr_name = name
        self._host = host
        self._port = port
        self._last_image = None

    async def async_camera_image(self, width=None, height=None):
        return self._last_image

    async def fetch_image(self, picture_index):
        command = bytes([0x0B, 0xB0, 0x00, 0x00, 0x00, picture_index])
        try:
            reader, writer = await asyncio.open_connection(self._host, self._port)
            writer.write(command)
            await writer.drain()
            chunks = []
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                chunks.append(data)
            self._last_image = b''.join(chunks)
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            _LOGGER.error("Erro ao requisitar imagem: %s", e)
