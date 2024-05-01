from pydantic import BaseModel


class GitHubLinkModel(BaseModel):
    link: str
    user_name: str
    repository_name: str
    task: str | None = None
    params: str | None = None