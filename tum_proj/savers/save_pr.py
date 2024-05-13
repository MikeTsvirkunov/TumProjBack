from random import choice
from typing import List
import uuid
import ioc
from tum_proj.models.homework_models import PullRequestModel, StudentPullRequestForPassModel
from tum_proj.models.user_model import UserModel


def test_save_pr(user: UserModel, pr_for_pass: StudentPullRequestForPassModel):
    list_of_pr: List[PullRequestModel] = list(ioc.require('list_of_pr'))
    build_pull_rquest_model = ioc.require('build_pull_rquest_model')
    pr = build_pull_rquest_model(link=pr_for_pass.pr_link, username=user.loggin, pr_id=choice([str(uuid.uuid4, 'succes_checked_id')]))
    list_of_pr.append(pr)
    ioc.override('list_of_pr', list_of_pr)

