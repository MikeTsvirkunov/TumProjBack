from typing import List
import ioc
from tum_proj.models.user_model import UserModel


def registration_code_validator(registration_code: str):
    x: dict[str, UserModel] = list(ioc.require('dict_of_registrated_users'))
    for i in x:
        if i.registration_code == registration_code:
            return True
    return False