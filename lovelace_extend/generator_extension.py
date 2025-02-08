from abc import ABC, abstractmethod
from typing import Dict, Any
from .abstract_extension import Extension
from orjson import Fragment


class GeneratorExtension(Extension, ABC):
    @abstractmethod
    def get_config(self) -> Dict[str, Any]:
        """
        config registering dashboard, see DASHBOARD_BASE_CREATE_FIELDS
        in homeassistant.components.lovelace.const
        """

    @abstractmethod
    def url_path(self) -> str:
        """
        Url path for frontend, should contain -
        """

    @abstractmethod
    async def async_load(self, force: bool) -> dict[str, Any]:
        """
        Get Config
        """

    @abstractmethod
    async def async_json(self, force: bool) -> Fragment:
        """
        Get config in json
        """