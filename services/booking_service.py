from datetime import timedelta

from constants import BOOKING_DURATION, RoomStatus, RoleId
from exceptions.booking_exceptions import *
from exceptions.auth_exceptions import AuthorizationError
from repositories.booking_repository import BookingRepository
from abstractions import RoomServiceInterface, AuthServiceInterface
from utils import generate_uuid
from models import Booking


class BookingService:
    def __init__(self, booking_repository, room_service, auth_service):
        self.booking_repository : BookingRepository = booking_repository
        self.room_service: RoomServiceInterface = room_service
        self.auth_service: AuthServiceInterface = auth_service


    async def create_booking(self, payload, user_id) -> Booking:
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

        return booking


    async def get_user_bookings(self, user_id) -> list[Booking]:
        bookings = await self.booking_repository.get_user_bookings(user_id)

        if not bookings:
            return []

        return bookings


    async def get_booking_details(self, booking_id, user_id) -> Booking:
        user_with_role = await self.auth_service.get_user_with_role(user_id)

        booking = await self.booking_repository.get_booking_details(booking_id)

        if user_with_role.role.name == RoleId.ADMIN.value:
            return booking

        if booking.user_id!=user_id:
            raise AuthorizationError()

        return booking


    async def delete_booking(self, booking_id, user_id):
        user_with_role =await self.auth_service.get_user_with_role(user_id)

        booking = await self.booking_repository.get_booking_details(booking_id)

        if not booking:
            raise BookingNotFoundError()

        if (
            user_with_role.role.name != RoleId.ADMIN.value
            and booking.user_id!=user_id
        ):
            raise AuthorizationError()

        await self.booking_repository.delete_booking(booking)




