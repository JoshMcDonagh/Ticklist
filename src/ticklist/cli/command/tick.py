from datetime import datetime
from typing import Dict, Any, List

from src.ticklist import get_open_task_list, get_closed_task_list
from src.ticklist.cli.command import Command
from src.ticklist.schemas import TASK_NO_TYPE
from src.ticklist.task import Task


class Tick(Command):
    @property
    def name(self) -> str:
        return "tick"

    @property
    def description(self) -> str:
        return "Marks task as complete"

    @property
    def expected_mandatory_args(self) -> List[type]:
        return [TASK_NO_TYPE]

    @property
    def expected_optional_args(self) -> Dict[str, type]:
        return {}

    def execute(self, mandatory_args: list, optional_args: Dict[str, Any]) -> None:
        open_task_list = get_open_task_list()
        closed_task_list = get_closed_task_list()

        task_no = str(mandatory_args[0])

        task = open_task_list.get_task(task_no)
        open_task_list.remove_task(task_no)

        description = task.description
        creation_date = task.creation_date
        due_date = task.due_date
        completion_date = datetime.now()

        closed_task_list.add_task(
            Task(
                task_no=task_no,
                description=description,
                creation_date=creation_date,
                due_date=due_date,
                completion_date=completion_date
            )
        )
