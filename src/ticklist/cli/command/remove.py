from typing import Dict, Any, List

from src.ticklist import get_open_task_list, get_closed_task_list
from src.ticklist.cli.command import Command
from src.ticklist.schemas import TASK_NO_TYPE


class Remove(Command):
    @property
    def name(self) -> str:
        return "remove"

    @property
    def description(self) -> str:
        return "Removes a task"

    @property
    def mandatory_args(self) -> List[type]:
        return [TASK_NO_TYPE]

    @property
    def optional_args(self) -> Dict[str, type]:
        return {}

    def execute(self, actual_mandatory_args: list, actual_optional_args: Dict[str, Any]) -> None:
        open_task_list = get_open_task_list()
        closed_task_list = get_closed_task_list()

        task_no = str(actual_mandatory_args[0])

        if open_task_list.is_exists(task_no):
            open_task_list.remove_task(task_no)

        if closed_task_list.is_exists(task_no):
            closed_task_list.remove_task(task_no)
