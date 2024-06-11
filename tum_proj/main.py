from datetime import datetime

import ioc
from tum_proj.constants import UserType
from tum_proj.getters.get_comments_on_pr import get_pr_comments
from tum_proj.initiators import init_values
from tum_proj.models import LastCheckedPR, WorkingSession
from tum_proj.psql_python import check_student, check_teacher, create_teacher, create_student, create_pull_request, select_pr_by_teacher_id
from fastapi import FastAPI, HTTPException
import uuid
# from tum_proj.processors.links_processors import split_github_link
from tum_proj.requests_bodies import CheckIsPreviousPRCheckedBody, PullRequestDescription, SendCheckedPRForCheck, Student, Teacher, User
from tum_proj.test_data import PullRequestData
from tum_proj.validators.validate_auth_key import validate_auth_key
from fastapi.middleware.cors import CORSMiddleware




init_values()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/is_running")
async def is_running():
    return {"message": "running"}


@app.post("/get_auth_key")
async def get_auth_key(user: User):
    new_id = str(uuid.uuid4())
    r = {'success': False}
    l = list(ioc.require('WorkingSession.ListOfSessions'))
    if user.login == 'test_teacher':
        l.append(WorkingSession(user_type=UserType.teacher, working_id=new_id, create_time=datetime.now(), user_id=-1))
        r = {"auth_key": new_id, 'user_type': UserType.teacher, 'success': True}
    elif user.login == 'test_student':
        l.append(WorkingSession(user_type=UserType.student, working_id=new_id, create_time=datetime.now(), user_id=-1))
        r = {"auth_key": new_id, 'user_type': UserType.student, 'success': True}
    else:
        x1 = check_student(user.login, user.password)
        x2 = check_teacher(user.login, user.password)
        print(x1, x2)
        if len(x1) > 0:
            user_type = UserType.student
            user_id = list(x1)[0][0]
        elif len(x2) > 0:
            user_type = UserType.teacher
            print(x1)
            user_id = list(x2)[0][0]
        else:
            return {'success': False}
        l.append(WorkingSession(user_type=user_type, working_id=new_id, create_time=datetime.now(), user_id=user_id))
        r = {"auth_key": new_id, 'user_type': user_type, 'success': True}
    ioc.override('WorkingSession.ListOfSessions', l)
    return r


@app.post("/check_is_previous_pr_checked")
async def check_is_previous_pr_checked(body: CheckIsPreviousPRCheckedBody):
    if validate_auth_key(body.auth_key):
        d: dict[str, LastCheckedPR] = dict(ioc.require('WorkingSession.LastWatchedPR'))
        print(d)
        if not body.auth_key in d:
            return {'changes': True}
        lr = d[body.auth_key]
        cr = get_pr_comments(lr.pr_link)
        return {'changes': lr.comments != cr}
    raise HTTPException('Incorrect auth key')


@app.post("/send_checked_pr_to_check")
async def send_checked_pr_to_check(body: SendCheckedPRForCheck):
    if validate_auth_key(body.auth_key):
        cr = get_pr_comments(body.pr_link)
        d: dict[str, LastCheckedPR] = dict(ioc.require('WorkingSession.LastWatchedPR'))
        d[body.auth_key] = LastCheckedPR(pr_link=body.pr_link, comments=cr)
        ioc.override('WorkingSession.LastWatchedPR', d)
        return {'result: success'}
    raise HTTPException('Incorrect auth key')


@app.post("/create_pull_request")
async def create_pull(pr: PullRequestDescription):
    l: list[WorkingSession] = list(ioc.require('WorkingSession.ListOfSessions'))
    wsd = next(filter(lambda a: a.working_id == pr.auth_key, l))
    done = create_pull_request(pr.pull_link, pr.comment, wsd.user_id, pr.lr_num)
    result = { "res" : done}
    print(result)
    return result   


@app.post("/create_teacher")
async def create_teacher_request(teach: Teacher):
    done = create_teacher(teach.login, teach.password)
    result = { "res" : done}
    print(result)
    return result


@app.post("/create_student")
async def create_student_request(stud: Student):
    done = create_student(stud.login, stud.password, stud.teacher)
    result = { "res" : done}
    print(result)
    return result


@app.get("/get_pr_by_teacher")
async def get_pr_by_teacher_request(teacher_id):
    l: list[WorkingSession] = list(ioc.require('WorkingSession.ListOfSessions'))
    uid = next(filter(lambda a: a.working_id, l)).user_id
    print(uid)
    if uid == -1:
        pr = {'data': PullRequestData().data}
    else:
        print(teacher_id)
        pr = {'data': select_pr_by_teacher_id(uid)}
    # print(pr)
    
    return pr


# @app.post("/get_pull_request")
# async def get_pull_request(link: PullRequestDescription):
#     print(link.link)
#     return split_github_link(link.link).model_dump_json()
