from abc import ABC, abstractmethod
from typing import Any, Dict
from homeassistant.core import HomeAssistant


class FilterExtension(ABC):

    _hass: HomeAssistant

    def __init__(self, hass: HomeAssistant):
        self._hass = hass

    def supports(self, environment: str) -> bool:
        """
        should return true when these filters should be added to given environment
        possible environments are template.environment, template.environment_limited
        template.environment_strict and template.environment_<dashboard id>
        """

    @abstractmethod
    def filters(self) -> Dict[str, Any]:
        pass
