from datetime import timedelta

from constants import BOOKING_DURATION, RoomStatus
from exceptions.booking_exceptions import RoomNotAvailableError, CannotCreateBookingError
from repositories.booking_repository import BookingRepository
from abstractions import RoomServiceInterface
from utils import generate_uuid


class BookingService:
    def __init__(self, booking_repository, room_service):
        self.booking_repository : BookingRepository = booking_repository
        self.room_service: RoomServiceInterface = room_service

    async def create_booking(self, payload, user_id):
        start_time = payload.start_time
        room_id = payload.room_id
        end_time = start_time + timedelta(hours=int(BOOKING_DURATION))

        room = await self.room_service.get_room_details(room_id)
        if not room or room.status != RoomStatus.ACTIVE.value:
            raise RoomNotAvailableError()

        booking_id = generate_uuid()
        booking = await self.booking_repository.create_booking(
            id = booking_id,
            user_id = user_id,
            room_id = room_id,
            start_time = start_time,
            end_time = end_time
        )

        if not booking :
            raise CannotCreateBookingError()

    async def get_user_bookings(self, user_id):
        pass

    async def get_booking_details(self, booking_id, user_id):
        pass

    async def delete_booking(self, booking_id, user_id):
        pass