import pandas as pd

from src.config.paths import OPEN_TASKS_JSON
from src.ticklist.task_list import TaskList


class OpenTaskList(TaskList):
    def __init__(self):
        super().__init__(OPEN_TASKS_JSON)

    @property
    def _dataframe_structure(self) -> dict:
        return {
            "id": pd.Series(dtype="str"),
            "creation_date": pd.Series(dtype="datetime64[ns]"),
            "name": pd.Series(dtype="str"),
            "description": pd.Series(dtype="str"),
            "due_date": pd.Series(dtype="datetime64[ns]")
        }
