from typing import List
from random import choice, randint
import uuid
from tum_proj.models.homework_models import PullRequestForCheckModel
from tum_proj.models.user_model import UserModel


def test_get_list_of_pr(user: UserModel, num: int) -> List[PullRequestForCheckModel]:
    username = ''.join([choice('asdfghjklqwertyuip') for i in range(randint(5, 15))])
    username += ' '
    username += ''.join([choice('asdfghjklqwertyuip') for i in range(randint(5, 15))])
    return [
        PullRequestForCheckModel(
            pr_id=str(uuid.uuid4()),
            link='https://github.com/BallBoychick/APITrain/pull/3', 
            username=username, 
            num_of_pass_labs=randint(0, 5), 
            num_of_try=randint(0, 5)
            ) 
        for _ in range(num)
    ]