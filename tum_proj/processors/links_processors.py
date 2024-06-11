# from tum_proj.models.git_models import GitHubLinkModel

from pydantic import BaseModel


class GitHubLinkModel(BaseModel):
    link: str
    user_name: str
    repository_name: str
    task: str | None = None
    params: str | None = None

def split_github_link(link: str) -> GitHubLinkModel:
    d = link.split('github.com/')[1].split('?')[0].split('/')
    print(d)
    return GitHubLinkModel(
        link=link,
        user_name=d[0],
        repository_name=d[1],
        task=d[2] if len(d) >= 3 else None,
        params=d[3] if len(d) >= 4 else None
    )
