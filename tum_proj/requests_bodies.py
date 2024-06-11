from pydantic import BaseModel


class Link(BaseModel):
    link: str

class Teacher(BaseModel):
    login: str
    password : str

class Student(BaseModel):
    login: str
    password : str
    teacher: str


class User(BaseModel):
    login: str
    password : str


class PullRequestDescription(BaseModel):
    # pull_request_id: str
    lr_num: int
    auth_key: str
    pull_link: str
    comment: str


class CheckIsPreviousPRCheckedBody(BaseModel):
    auth_key: str


class SendCheckedPRForCheck(BaseModel):
    auth_key: str
    pr_link: str