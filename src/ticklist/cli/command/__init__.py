from abc import ABC, abstractmethod
from typing import Dict


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
    def expected_args(self) -> Dict[str, type]:
        pass

    @abstractmethod
    def execute(self, args: list):
        pass