from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Any

from src.ticklist.cli.command.add import Add
from src.ticklist.cli.command.remove import Remove
from src.ticklist.cli.command.tick import Tick

_AVAILABLE_COMMANDS: Dict[str, Command] | None = None

def _make_command_dict(commands: List[Command]) -> Dict[str, Command]:
    command_dict = {}
    for command in commands:
        command_dict[command.name] = command
    return command_dict


def get_command(command_name: str) -> Command:
    global _AVAILABLE_COMMANDS

    if _AVAILABLE_COMMANDS is None:
        _AVAILABLE_COMMANDS = _make_command_dict([
            Add(),
            Remove(),
            Tick()
        ])

    return _AVAILABLE_COMMANDS[command_name]


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
    def mandatory_args(self) -> Dict[str, MandatoryArgument]:
        pass

    @property
    @abstractmethod
    def optional_args(self) -> Dict[str, OptionalArgument]:
        pass

    @abstractmethod
    def execute(
            self,
            actual_mandatory_args: Dict[str, MandatoryArgument],
            actual_optional_args: Dict[str, OptionalArgument]
    ) -> None:
        pass

    @staticmethod
    def _make_arg_dict(
            args: List[MandatoryArgument | OptionalArgument]
    ) -> Dict[str, MandatoryArgument | OptionalArgument]:
        arg_dict = {}
        for arg in args:
            if arg is MandatoryArgument:
                arg_dict[arg.name] = arg
            elif arg is OptionalArgument:
                arg_dict[arg.short_tag] = arg
            else:
                raise ValueError("Argument must be Mandatory or Optional")
        return arg_dict
