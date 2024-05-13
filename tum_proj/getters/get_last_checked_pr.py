import ioc
from tum_proj.models.user_model import UserModel


def get_last_checked_pr(user: UserModel):
    dict_of_last_past_checked = dict(ioc.require('dict_of_last_past_checked'))
    if user.user_id in dict_of_last_past_checked: 
        return dict_of_last_past_checked[user.user_id]
    return None