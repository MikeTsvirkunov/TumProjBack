from pydantic import BaseModel


class ValidateForPRCheckedModel(BaseModel):
    validation_code: str