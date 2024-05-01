from tum_proj.models.git_models import GitHubLinkModel


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
