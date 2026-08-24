from datetime import datetime
from pydantic import BaseModel


class CreateBookingRequest(BaseModel):
    room_id : str
    start_time : datetime




