from abc import ABC, abstractmethod
from typing import Dict, Callable
from .abstract_extension import Extension

class TestExtension(Extension, ABC):

    @abstractmethod
    def tests(self) -> Dict[str, Callable[..., bool]]:
        pass
