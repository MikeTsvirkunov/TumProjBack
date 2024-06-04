from tum_proj.psql_python import send_to_db_html_content, create_teacher, create_student, create_pull_request, select_pr_by_teacher_id, check_student
from pydantic import BaseModel
from tum_proj.getters.get_git_page import get_github_page
# from tum_proj.initiators import std_initiation
from tum_proj.models.git_models import GitHubLinkModel
from fastapi import FastAPI
import uuid

from tum_proj.processors.links_processors import split_github_link
# std_initiation()
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
        return split_github_link(link.link).model_dump_json()
    return split_github_link(link.link).model_dump_json()

class Teacher(BaseModel):
    login: str
    password : str

class Student(BaseModel):
    login: str
    password : str

class PullRequestDescription(BaseModel):
    # pull_request_id: str
    pull_link: str
    comment: str




@app.post("/create_pull_request")
async def create_pull(pr: PullRequestDescription):
    done = create_pull_request(pr.pull_link, pr.comment)

    result = { "res" : done}

    print(result)
    
    return result

@app.post("/create_teacher")
async def create_teacher_request(teach: Teacher):
    done = create_teacher(teach.login, teach.password)

    result = { "res" : done}

    print(result)
    
    return result

@app.post("/check_student")
async def check_student_request(stud: Student):
    done = check_student(stud.login, stud.password)

    if len(done) != 0:
        result = True
    else:
        result = False

    print(result)
    
    return result

@app.post("/create_student")
async def create_student_request(stud: Student):
    done = create_student(stud.login, stud.password)

    result = { "res" : done}

    print(result)
    
    return result

@app.get("/get_pr_by_teacher")
async def get_pr_by_teacher_request(teacher_id):
    pr = select_pr_by_teacher_id(teacher_id)
    print(pr)
    return pr

@app.post("/get_pull_request")
async def get_pull_request(link: PullRequestDescription):
    print(link.link)
    return split_github_link(link.link).model_dump_json()