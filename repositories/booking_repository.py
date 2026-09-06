import datetime

from models import Booking
from sqlalchemy import Select

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


    async def get_user_bookings(self, user_id : str):
        result = await self.db.execute(
            Select(Booking).where(Booking.user_id == user_id)
        )
        if not result:
            return []

        bookings = result.scalars().all()
        return bookings


    async def get_booking_details(self, booking_id : str)->Booking | None:
        booking = await self.db.scalar(
            Select(Booking).where(Booking.id == booking_id)
        )

        return booking


    async def delete_booking(self, booking : Booking):
        await self.db.delete(booking)
        await self.db.commit()

