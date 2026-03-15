from abc import ABC, abstractmethod
from typing import Dict, List, Any


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
    def expected_mandatory_args(self) -> List[type]:
        pass

    @property
    @abstractmethod
    def expected_optional_args(self) -> Dict[str, type]:
        pass

    @abstractmethod
    def execute(self, mandatory_args: list, optional_args: Dict[str, Any]) -> None:
        pass
