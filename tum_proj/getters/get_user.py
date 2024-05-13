import ioc
from tum_proj.models.user_model import UserModel


def get_user_by_validation_code(validation_code: str) -> UserModel:
    dict_of_registrated_users: dict[str, UserModel] = dict(ioc.require('dict_of_registrated_users'))
    return dict_of_registrated_users[validation_code]