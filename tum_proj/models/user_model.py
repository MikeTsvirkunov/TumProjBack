from datetime import datetime
from pydantic import BaseModel


class UserModel(BaseModel):
    loggin: str
    user_id: str
    validation_code: str | None=None
    time_of_creation: datetime
    user_type: str
