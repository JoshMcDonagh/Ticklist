from src.ticklist.task_list.closed_task_list import ClosedTaskList
from src.ticklist.task_list.open_task_list import OpenTaskList

_open_task_list: OpenTaskList | None = None
_closed_task_list: ClosedTaskList | None = None


def get_open_task_list() -> OpenTaskList:
    global _open_task_list

    if _open_task_list is None:
        _open_task_list = OpenTaskList()

    return _open_task_list


def get_closed_task_list() -> ClosedTaskList:
    global _closed_task_list

    if _closed_task_list is None:
        _closed_task_list = ClosedTaskList()

    return _closed_task_list
