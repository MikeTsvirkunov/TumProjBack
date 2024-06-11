import requests
import json
from tum_proj.processors.links_processors import split_github_link


def get_pr_comments(pr_link: str):
    sl = split_github_link(pr_link)
    r = f'https://api.github.com/repos/{sl.user_name}/{sl.repository_name}/{sl.task+"s"}/{sl.params}'
    print(r)
    s = requests.get(r)
    s = s.json()
    s = {
        'comments': s['comments']
    }
    print(s)
    j = s
    # j = json.loads(s)
    return j