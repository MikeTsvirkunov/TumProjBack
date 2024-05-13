from datetime import datetime
from pydantic import BaseModel


class StudentPullRequestForPassModel(BaseModel):
    validation_code: str
    pr_link: str
    comment: str


class PullRequestModel(BaseModel):
    pr_id: str
    link: str
    username: str
    date: datetime


class PullRequestForCheckModel(BaseModel):
    pr_id: str
    link: str
    username: str
    num_of_pass_labs: int
    num_of_try: int
    date: datetime


class CheckingPullRequestModel(BaseModel):
    pr_id: str