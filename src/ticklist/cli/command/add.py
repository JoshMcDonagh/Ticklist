from datetime import datetime
from typing import Dict, Any, List

from src.ticklist import get_open_task_list, get_closed_task_list
from src.ticklist.cli.command import Command, MandatoryArgument, OptionalArgument
from src.ticklist.schemas import DESCRIPTION_TYPE, DUE_DATE_TYPE
from src.ticklist.task import Task

_DESCRIPTION_NAME = "description"
_DUE_DATE_S_TAG = "d"
_DUE_DATE_V_TAG = "due-date"


class Add(Command):
    @property
    def name(self) -> str:
        return "add"

    @property
    def description(self) -> str:
        return "Adds task to open task list"

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

    @property
    def mandatory_args(self) -> Dict[str, MandatoryArgument]:
        mandatory_args: List[MandatoryArgument] = [MandatoryArgument(
            name=_DESCRIPTION_NAME,
            type=DESCRIPTION_TYPE
        )]
        return self._make_arg_dict(mandatory_args)

    @property
    def optional_args(self) -> Dict[str, OptionalArgument]:
        optional_args: List[OptionalArgument] = [OptionalArgument(
            short_tag=_DUE_DATE_S_TAG,
            verbose_tag=_DUE_DATE_V_TAG,
            type=DUE_DATE_TYPE
        )]
        return self._make_arg_dict(optional_args)

    def execute(
            self,
            actual_mandatory_args: Dict[str, MandatoryArgument],
            actual_optional_args: Dict[str, OptionalArgument]
    ) -> None:
        open_task_list = get_open_task_list()
        closed_task_list = get_closed_task_list()

        num_of_tasks = open_task_list.num_of_tasks + closed_task_list.num_of_tasks

        task_no = str(num_of_tasks)
        description = actual_mandatory_args[_DESCRIPTION_NAME].value
        creation_date = datetime.now()
        due_date = actual_optional_args[_DUE_DATE_S_TAG].value
        completion_date = None

        open_task_list.add_task(
            Task(
                task_no=task_no,
                description=description,
                creation_date=creation_date,
                due_date=due_date,
                completion_date=completion_date
            )
        )
