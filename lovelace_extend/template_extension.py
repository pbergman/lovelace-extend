from abc import ABC
from .abstract_extension import Extension


class TemplateExtension(Extension, ABC):
    def supports(self, environment: str) -> bool:
        """
        should return true when filters or tests should be added to given environment
        possible environments are template.environment, template.environment_limited
        template.environment_strict and template.environment_<dashboard id> for the
        custom environment build to render the dashboard config
        """
