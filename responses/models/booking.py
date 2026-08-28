from pydantic import BaseModel, ConfigDict
from datetime import datetime

class BookingCreateResponse(BaseModel):
    id : str
    room_id : str
    start_time : datetime
    end_time : datetime

    model_config = ConfigDict(from_attributes = True)


class BookingsFetchResponse(BaseModel):
    id : str
    room_id : str
    start_time : datetime
    end_time : datetime

    model_config = ConfigDict(from_attributes = True)