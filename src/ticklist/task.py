from dataclasses import dataclass

from src.ticklist.schemas import TASK_NO_TYPE, DESCRIPTION_TYPE, CREATION_DATE_TYPE, DUE_DATE_TYPE, \
    COMPLETION_DATE_TYPE


@dataclass
class Task:
    task_no: TASK_NO_TYPE
    description: DESCRIPTION_TYPE
    creation_date: CREATION_DATE_TYPE
    due_date: DUE_DATE_TYPE
    completion_date: COMPLETION_DATE_TYPE
