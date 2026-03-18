from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class MandatoryArgument:
    name: str
    type: type
    value: Any | None = None

@dataclass
class OptionalArgument:
    short_tag: str
    verbose_tag: str
    type: type | None = None
    default: Any = None
    action: str = None
    value: Any | None = None


class Command(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def mandatory_args(self) -> List[MandatoryArgument]:
        pass

    @property
    @abstractmethod
    def optional_args(self) -> List[OptionalArgument]:
        pass

    @abstractmethod
    def execute(
            self,
            actual_mandatory_args: List[MandatoryArgument],
            actual_optional_args: List[OptionalArgument]
    ) -> None:
        pass
