from abc import ABC, abstractmethod
from typing import Dict, Callable
from homeassistant.core import HomeAssistant


class TestExtension(ABC):

    _hass: HomeAssistant

    def __init__(self, hass: HomeAssistant):
        self._hass = hass

    def supports(self, environment: str) -> bool:
        """
        should return true when these tesst should be added to given environment
        possible environments are template.environment, template.environment_limited
        template.environment_strict and template.environment_<dashboard id>
        """

    @abstractmethod
    def tests(self) -> Dict[str, Callable[..., bool]]:
        pass
