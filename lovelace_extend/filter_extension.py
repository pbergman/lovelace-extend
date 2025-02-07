from abc import ABC, abstractmethod
from typing import Any, Dict
from .template_extension import TemplateExtension


class FilterExtension(TemplateExtension, ABC):

    @abstractmethod
    def filters(self) -> Dict[str, Any]:
        pass
