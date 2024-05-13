import uuid
from tum_proj.models.registration_models import RegistrationModel


def uuid_registration_code_getter(acc: RegistrationModel):
    return str(uuid.uuid4())