import pandas as pd

from src.config.paths import OPEN_TASKS_JSON
from src.ticklist.schemas import create_open_task_list_schema_dict, TASK_NO_LABEL
from src.ticklist.list.task_list import TaskList
from src.ticklist.task import Task


class OpenTaskList(TaskList):
    def __init__(self):
        super().__init__(OPEN_TASKS_JSON)

    @property
    def _dataframe_schema(self) -> dict:
        return create_open_task_list_schema_dict()

    def add_task(self, task: Task) -> None:
        tasks_dataframe: pd.DataFrame = super()._tasks_dataframe
        tasks_dataframe.loc[len(tasks_dataframe)] = [
            task.task_no,
            task.description,
            task.creation_date,
            task.due_date
        ]

        if super()._does_dataframe_follow_schema(tasks_dataframe):
            super()._tasks_dataframe = tasks_dataframe
        else:
            raise ValueError("Task list does not follow the expected schema after adding task.")
