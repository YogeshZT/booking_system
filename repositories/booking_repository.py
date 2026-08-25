import datetime
from models import Booking


class BookingRepository:
    def __init__(self, db):
        self.db = db

    async def create_booking(self, id: str, user_id :str, room_id : str, start_time : str, end_time : datetime) -> Booking | None:
        booking = Booking(
            id = id,
            room_id=room_id,
            user_id=user_id,
            start_time=start_time,
            end_time=end_time,
        )

        self.db.add(booking)
        await self.db.commit()
        await self.db.refresh(booking)

        return booking


