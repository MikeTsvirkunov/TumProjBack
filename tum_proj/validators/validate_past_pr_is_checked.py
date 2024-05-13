from tum_proj.models.homework_models import PullRequestModel


def test_validate_past_pr_is_checked(pr: PullRequestModel) -> bool:
    return pr.pr_id == 'succes_checked_id'