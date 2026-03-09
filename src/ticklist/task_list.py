from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class TaskList(ABC):
    def __init__(self, json_file_path: Path):
        self._json_file_path: Path = json_file_path
        self._dataframe: pd.DataFrame | None = None

    @abstractmethod
    @property
    def _dataframe_structure(self) -> dict:
        pass

    def _create_empty_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._dataframe_structure)

    def _make_sure_dir_exists(self) -> None:
        self._json_file_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> None:
        self._make_sure_dir_exists()
        if self._json_file_path.exists():
            self._dataframe = pd.read_json(self._json_file_path, orient="table")
        else:
            self._dataframe = self._create_empty_dataframe()

    def save(self) -> None:
        self._make_sure_dir_exists()
        self._dataframe.to_json(self._json_file_path, orient="table")
