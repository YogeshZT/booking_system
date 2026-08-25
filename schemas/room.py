from pydantic import BaseModel


class RoomCreationRequest(BaseModel):
    room_name : str

class RoomEditRequest(BaseModel):
    new_room_name : str
    room_id : str