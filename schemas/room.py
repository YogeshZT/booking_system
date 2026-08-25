from pydantic import BaseModel


class RoomCreationRequest(BaseModel):
    room_name : str