import argparse
import shlex
from typing import Dict, List, Any, Tuple

from src.ticklist.cli.command import Command

_parser = argparse.ArgumentParser()




class Parser:
    def __init__(self):
        self._commands: Dict[str, Command] = {}

    def add_command(self, command: Command) -> None:
        self._commands[command.name] = command

    @staticmethod
    def _get_tokens_from_command_line(command_line: str) -> List[str]:
        return shlex.split(command_line)

    def _get_command_from_tokens(self, tokens: List[str]) -> Command:
        command_name = tokens[0]
        try:
            return self._commands[command_name]
        except KeyError as e:
            raise ValueError(f'No command named "{command_name}"') from e

    @staticmethod
    def _get_args_from_tokens(command: Command, tokens: List[str]) -> Tuple[List[Any], Dict[str, Any]]:
        args = tokens[1:]

        # --- Parse mandatory arguments ---

        expected_mandatory_args: List[type] = command.mandatory_args
        mandatory_args: List[Any] = []
        for expected_arg_type in expected_mandatory_args:
            if not args:
                raise ValueError(f'Missing expected argument of type "{expected_arg_type.__name__}"')
            arg = args.pop(0)
            try:
                mandatory_args.append(expected_arg_type(arg))
            except (ValueError, TypeError) as e:
                raise ValueError(
                    f"Invalid argument provided: '{arg}' must be of type {expected_arg_type.__name__}") from e

        if len(args) % 2 != 0:
            raise ValueError("Optional arguments must be provided as tag-value pairs")

        # --- Parse optional arguments ---

        arg_pairs = zip(args[::2], args[1::2])

        expected_optional_args: Dict[str, type] = command.optional_args
        optional_args: Dict[str, Any] = {}
        for arg_tag, arg_val in arg_pairs:
            if arg_tag not in expected_optional_args:
                raise ValueError(f"Invalid tag provided: '{arg_tag}'")
            if arg_tag in optional_args:
                raise ValueError(f"Duplicate tag provided: '{arg_tag}'")

            expected_arg_type = expected_optional_args[arg_tag]
            try:
                arg_val = expected_arg_type(arg_val)
            except (ValueError, TypeError) as e:
                raise ValueError(
                    f"Invalid argument provided: '{arg_val}' must be of type {expected_arg_type.__name__}") from e

            optional_args[arg_tag] = arg_val

        return mandatory_args, optional_args

    def parse_and_execute(self, command_line: str) -> None:
        tokens = self._get_tokens_from_command_line(command_line)
        if not tokens:
            return
        command = self._get_command_from_tokens(tokens)
        mandatory_args, optional_args = self._get_args_from_tokens(command, tokens)
        command.execute(mandatory_args, optional_args)
