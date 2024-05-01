from pydantic import BaseModel
from tum_proj.getters.get_git_page import get_github_page
from tum_proj.models.git_models import GitHubLinkModel
from fastapi import FastAPI
import uuid

from tum_proj.processors.links_processors import split_github_link

app = FastAPI()


@app.get("/is_running")
async def root():
    return {"message": "running"}

class Link(BaseModel):
    link: str


# https://github.com/MikeTsvirkunov/TestGHApiRep/pull/2
@app.post("/send_pull_request")
async def send_pull_request(link: Link):
    link_model = split_github_link(link.link)
    if link_model.task == 'pull':
        page = get_github_page(link_model.link)
        with open(f'../{uuid.uuid4()}.html', 'w') as f:
            f.write(page)
        return 
    return split_github_link(link.link).model_dump_json()

class PullRequestDescription(BaseModel):
    pull_request_id: str

@app.post("/get_pull_request")
async def get_pull_request(link: PullRequestDescription):
    print(link.link)
    return split_github_link(link.link).model_dump_json()
    