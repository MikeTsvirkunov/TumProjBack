from datetime import datetime
from pydantic import BaseModel


class WorkingSession(BaseModel):
    user_type: str
    working_id: str
    create_time: datetime
    user_id: int


class LastCheckedPR(BaseModel):
    pr_link: str
    comments: dict