from pydantic import BaseModel


class GetListOfPrModel(BaseModel):
    num: int
    validation_code: str