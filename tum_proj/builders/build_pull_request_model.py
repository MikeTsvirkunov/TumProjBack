import datetime
from tum_proj.models.homework_models import PullRequestModel


def build_pull_rquest_model(**args) -> PullRequestModel:
    return PullRequestModel(
        pr_id=args['pr_id'],
        link=args['link'],
        username=args['username'],
        date=datetime.datetime.now()
    )