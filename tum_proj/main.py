import ioc
from tum_proj.initiators import functions_initialization, values_initiation
from fastapi import FastAPI, HTTPException
from tum_proj.models.get_list_of_pr_models import GetListOfPrModel
from tum_proj.models.homework_models import CheckingPullRequestModel, StudentPullRequestForPassModel
from tum_proj.models.registration_models import RegistrationModel
import sys

from tum_proj.models.user_model import UserModel
from tum_proj.models.validate_for_pr_checked_model import ValidateForPRCheckedModel
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)


values_initiation()
functions_initialization()


app = FastAPI()


@app.get("/is_running")
async def root():
    return {"message": "running"}


@app.post("/registration/")
def registration(acc: RegistrationModel):
    registration_validation = ioc.require('registration_validator')
    registration_code_getter = ioc.require('registration_code_getter')
    dict_of_registrated_users: dict[str, UserModel] = dict(ioc.require('dict_of_registrated_users'))
    build_user_model = ioc.require('build_user_model')
    if registration_validation(acc=acc):
        registration_code = registration_code_getter(acc=acc)
        dict_of_registrated_users[registration_code] = build_user_model(acc=acc)
        ioc.override('dict_of_registrated_users', dict_of_registrated_users)
        return registration_code
    raise HTTPException(status_code=401, detail="Incorrect parameters registration")


@app.post("/send_pull_request")
def send_pull_request(pr: StudentPullRequestForPassModel):
    get_user_by_validation_code = ioc.require('get_user_by_validation_code')
    save_pr = ioc.require('save_pr')
    user = get_user_by_validation_code(pr.validation_code)
    save_pr(user=user, pr_for_pass=pr)
    return {
        'save': 'ok'
    }


@app.get("/get_pull_requests_for_check/")
def get_passed_pull_requests(request: GetListOfPrModel):
    get_list_of_pr = ioc.require('get_list_of_pr')
    get_user_by_validation_code = ioc.require('get_user_by_validation_code')
    user = get_user_by_validation_code(request.validation_code)
    return {"list_for_check": get_list_of_pr(user=user, num=request.num)}


@app.post("/send_checking_pr")
def send_checking_pr(request: ValidateForPRCheckedModel):
    get_user_by_validation_code = ioc.require('get_user_by_validation_code')
    user = get_user_by_validation_code(request.validation_code)
    validate_past_pr_is_checked = ioc.require('validate_past_pr_is_checked')
    get_last_checked_pr = ioc.require('get_last_checked_pr')
    last_checked_pr = get_last_checked_pr()
    if last_checked_pr == None:
        return {'last_pr': 'doesn\'t exist'}
    is_checked = validate_past_pr_is_checked()
    return {'is_checked': is_checked}


@app.post("/get_pr")
def send_checking_pr(request: ValidateForPRCheckedModel):
    get_list_of_pr = ioc.require('get_list_of_pr')
    get_user_by_validation_code = ioc.require('get_user_by_validation_code')
    user = get_user_by_validation_code(request.validation_code)
    return None