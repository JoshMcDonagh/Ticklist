from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: str
    creation_date: datetime
    name: str
    description: str | None
    due_date: datetime | None
    is_completed: bool | None
    completed_date: datetime | None
