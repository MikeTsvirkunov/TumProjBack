import datetime
from tum_proj.models.registration_models import RegistrationModel
from tum_proj.models.user_model import UserModel


def test_build_user_model(acc: RegistrationModel):
    if acc.loggin == 'test_teacher':
        return UserModel(loggin=acc.loggin, user_type='teacher', time_of_creation=datetime.datetime.now(), user_id='teacher123')
    elif acc.loggin == 'test_student':
        return UserModel(loggin=acc.loggin, user_type='student', time_of_creation=datetime.datetime.now(), user_id='student123')
    raise Exception('User don\'t find')