from pydantic import BaseModel, ConfigDict
from datetime import datetime


class RoomResponse(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes = True)


class RoomCreateResponse(BaseModel):
    id : str
    name : str

    model_config = ConfigDict(from_attributes = True)


class RoomDetailsResponse(BaseModel):
    id : str
    name : str
    status : str
    created_at : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes = True)