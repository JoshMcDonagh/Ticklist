from datetime import datetime

import pandas as pd

TASK_NO_LABEL = "task_no"
DESCRIPTION_LABEL = "description"
CREATION_DATE_LABEL = "creation_date"
DUE_DATE_LABEL = "due_date"
COMPLETION_DATE_LABEL = "completion_date"

TASK_NO_TYPE = str
DESCRIPTION_TYPE = str
CREATION_DATE_TYPE = datetime
DUE_DATE_TYPE = datetime | None
COMPLETION_DATE_TYPE = datetime | None

TASK_NO_SERIES_TYPE = "str"
DESCRIPTION_SERIES_TYPE = "str"
CREATION_DATE_SERIES_TYPE = "datetime64[ns]"
DUE_DATE_SERIES_TYPE = "datetime64[ns]"
COMPLETION_DATE_SERIES_TYPE = "datetime64[ns]"


def create_open_task_list_schema_dict() -> dict:
    return {
        TASK_NO_LABEL: pd.Series(dtype=TASK_NO_SERIES_TYPE),
        DESCRIPTION_LABEL: pd.Series(dtype=DESCRIPTION_SERIES_TYPE),
        CREATION_DATE_LABEL: pd.Series(dtype=CREATION_DATE_SERIES_TYPE),
        DUE_DATE_LABEL: pd.Series(dtype=COMPLETION_DATE_SERIES_TYPE)
    }


def create_closed_task_list_schema_dict() -> dict:
    return {
        TASK_NO_LABEL: pd.Series(dtype=TASK_NO_SERIES_TYPE),
        DESCRIPTION_LABEL: pd.Series(dtype=DESCRIPTION_SERIES_TYPE),
        CREATION_DATE_LABEL: pd.Series(dtype=CREATION_DATE_SERIES_TYPE),
        DUE_DATE_LABEL: pd.Series(dtype=DUE_DATE_SERIES_TYPE),
        COMPLETION_DATE_LABEL: pd.Series(dtype=COMPLETION_DATE_SERIES_TYPE)
    }
