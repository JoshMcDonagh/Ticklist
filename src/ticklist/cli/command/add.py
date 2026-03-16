from datetime import datetime
from typing import Dict, Any, List

from src.ticklist import get_open_task_list, get_closed_task_list
from src.ticklist.cli.command import Command
from src.ticklist.schemas import DESCRIPTION_TYPE, DUE_DATE_TYPE
from src.ticklist.task import Task

_DUE_DATE_TAG_NAME = "--due-date"


class Add(Command):
    @property
    def name(self) -> str:
        return "add"

    @property
    def description(self) -> str:
        return "Adds task to open task list"

    @property
    def expected_mandatory_args(self) -> List[type]:
        return [DESCRIPTION_TYPE]

    @property
    def expected_optional_args(self) -> Dict[str, type]:
        return {_DUE_DATE_TAG_NAME: DUE_DATE_TYPE}

    def execute(self, mandatory_args: list, optional_args: Dict[str, Any]) -> None:
        open_task_list = get_open_task_list()
        closed_task_list = get_closed_task_list()

        num_of_tasks = open_task_list.num_of_tasks + closed_task_list.num_of_tasks

        task_no = str(num_of_tasks)
        description = mandatory_args[0]
        creation_date = datetime.now()
        due_date = optional_args[_DUE_DATE_TAG_NAME] if _DUE_DATE_TAG_NAME in optional_args else None
        completion_date = None

        task = Task(
            task_no=task_no,
            description=description,
            creation_date=creation_date,
            due_date=due_date,
            completion_date=completion_date
        )

        open_task_list.add_task(task)
