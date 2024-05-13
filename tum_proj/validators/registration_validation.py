from tum_proj.models.registration_models import RegistrationModel


def test_registration_validator(acc: RegistrationModel):
    if acc.loggin == 'test_teacher' and acc.password == 'test_teacher':
        return True
    elif acc.loggin == 'test_user' and acc.password == 'test_user':
        return True
    else:
        return False
    