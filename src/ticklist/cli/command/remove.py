from typing import Dict, Any, List

from src.ticklist import get_open_task_list, get_closed_task_list
from src.ticklist.cli.command import Command, MandatoryArgument, OptionalArgument
from src.ticklist.schemas import TASK_NO_TYPE

_TASK_NO_NAME = "task_no"


class Remove(Command):
    @property
    def name(self) -> str:
        return "remove"

    @property
    def description(self) -> str:
        return "Removes a task"

    @property
    def mandatory_args(self) -> Dict[str, MandatoryArgument]:
        mandatory_args: List[MandatoryArgument] = [MandatoryArgument(
            name=_TASK_NO_NAME,
            type=TASK_NO_TYPE
        )]
        return self._make_arg_dict(mandatory_args)

    @property
    def optional_args(self) -> Dict[str, OptionalArgument]:
        return {}

    def execute(
            self,
            actual_mandatory_args: Dict[str, MandatoryArgument],
            actual_optional_args: Dict[str, OptionalArgument]
    ) -> None:
        open_task_list = get_open_task_list()
        closed_task_list = get_closed_task_list()

        task_no = str(actual_mandatory_args[_TASK_NO_NAME])

        if open_task_list.is_exists(task_no):
            open_task_list.remove_task(task_no)

        if closed_task_list.is_exists(task_no):
            closed_task_list.remove_task(task_no)
