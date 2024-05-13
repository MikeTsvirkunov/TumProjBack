from pydantic import BaseModel


class RegistrationModel(BaseModel):
    loggin: str
    password: str
