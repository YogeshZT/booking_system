from pydantic import BaseModel


class SuccessResponse(BaseModel):
    status: int
    message: str
    data: dict
