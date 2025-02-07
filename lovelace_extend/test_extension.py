from abc import ABC, abstractmethod
from typing import Dict, Callable
from .template_extension import TemplateExtension


class TestExtension(TemplateExtension, ABC):

    @abstractmethod
    def tests(self) -> Dict[str, Callable[..., bool]]:
        pass
