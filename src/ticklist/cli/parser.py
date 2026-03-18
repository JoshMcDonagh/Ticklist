import argparse
import copy
import shlex
from typing import Dict, List, Any, Tuple

from src.ticklist.cli.command import Command, get_command


def parse_and_execute(self, command_line: str) -> None:
    parser = argparse.ArgumentParser()

    if command_line == "":
        return

    tokens = shlex.split(command_line)
    command_name = tokens.pop(0)
    try:
        command: Command = get_command(command_name)
    except Exception:
        print("Command not found")
        return

    mandatory_args = copy.deepcopy(command.mandatory_args)
    for arg in mandatory_args.values():
        parser.add_argument(
            arg.name,
            type=arg.type
        )

    optional_args = copy.deepcopy(command.optional_args)
    for arg in optional_args.values():
        parser.add_argument(
            f"-{arg.short_tag}",
            f"--{arg.verbose_tag}",
            type=arg.type,
            default=arg.default,
            action=arg.action
        )

    try:
        actual_args = parser.parse_args(tokens)
    except SystemExit:
        print("Invalid command")
        return

    for arg in mandatory_args.values():
        arg.value = getattr(actual_args, arg.name)

    for arg in optional_args.values():
        arg.value = getattr(actual_args, arg.verbose_tag)

    command.execute(mandatory_args, optional_args)
