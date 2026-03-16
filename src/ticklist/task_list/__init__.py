from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd
from tabulate import tabulate

from src.ticklist.schemas import TASK_NO_LABEL
from src.ticklist.task import Task


class TaskList(ABC):
    def __init__(self, json_file_path: Path):
        self._json_file_path: Path = json_file_path
        self._tasks_dataframe: pd.DataFrame | None = None
        self.load()

    @property
    @abstractmethod
    def _dataframe_schema(self) -> dict:
        pass

    @property
    def is_loaded(self) -> bool:
        return self._tasks_dataframe is not None

    @property
    def num_of_tasks(self) -> int:
        return self._tasks_dataframe.shape[0]

    def _does_dataframe_follow_schema(self, dataframe: pd.DataFrame) -> bool:
        schema = self._dataframe_schema

        if set(dataframe.columns) != set(schema.keys()):
            return False

        for column_name, expected_series in schema.items():
            if dataframe[column_name].dtype != expected_series:
                return False

        return True

    def _create_empty_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._dataframe_schema)

    def _make_sure_dir_exists(self) -> None:
        self._json_file_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> None:
        self._make_sure_dir_exists()
        if self._json_file_path.exists():
            dataframe = pd.read_json(self._json_file_path, orient="table")
            if not self._does_dataframe_follow_schema(dataframe):
                raise ValueError("Task list loaded from JSON does not follow the expected schema.")
            self._tasks_dataframe = dataframe
        else:
            self._tasks_dataframe = self._create_empty_dataframe()

    def save(self) -> None:
        if self.is_loaded:
            self._make_sure_dir_exists()
            self._tasks_dataframe.to_json(self._json_file_path, orient="table")
        else:
            raise RuntimeError("Task list has not been loaded.")

    def remove_task(self, task_no: str) -> None:
        tasks_dataframe = self._tasks_dataframe
        tasks_dataframe = tasks_dataframe[tasks_dataframe[TASK_NO_LABEL] != task_no]

        if self._does_dataframe_follow_schema(tasks_dataframe):
            self._tasks_dataframe = tasks_dataframe
        else:
            raise ValueError("Task list does not follow the expected schema after removing task.")

    @abstractmethod
    def add_task(self, task: Task) -> None:
        pass

    @abstractmethod
    def _get_formatted_dataframe(self, tasks_dataframe: pd.DataFrame) -> pd.DataFrame:
        pass

    def print(self) -> None:
        formatted_dataframe = self._get_formatted_dataframe(self._tasks_dataframe)
        print(tabulate(
            formatted_dataframe,
            tablefmt="rounded_outline",
            showindex=False
        ))
