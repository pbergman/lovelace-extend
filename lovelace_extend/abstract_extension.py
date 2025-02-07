from abc import ABC
from homeassistant.core import HomeAssistant


class Extension(ABC):
    """
    Base super class for all extensions
    """


class HassAwareExtension(ABC):
    """
    Base super to indicate we should be
    hass aware.

    class Foo(TestExtension, HassAwareExtension):
        ...
    """

    _hass: HomeAssistant

    def init(self, hass: HomeAssistant):
        self._hass = hass

