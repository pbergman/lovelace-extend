from abc import ABC, abstractmethod
from typing import Dict, Any
from .abstract_extension import Extension


class GeneratorExtension(Extension, ABC):
    @abstractmethod
    def get_config(self, force: bool = False) -> Dict[str, Any]:
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
    async def async_generate(self) -> Dict[str, Any]:
        """
        Build config dict.
        """
