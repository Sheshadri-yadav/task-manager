from datetime import time

from pydantic import BaseModel


class Tasks(BaseModel):

    task_title: str
    task_desc: str
    due_date: str
    due_time: time



