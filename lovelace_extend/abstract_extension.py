from abc import ABC
from homeassistant.core import HomeAssistant


class Extension(ABC):

    _hass: HomeAssistant

    def __init__(self, hass: HomeAssistant):
        self._hass = hass