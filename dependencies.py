from fastapi import Depends, Cookie

from infrastructure.database import get_db
from infrastructure.email_service import EmailService
from infrastructure.redis_db import get_redis_client

from repositories.booking_repository import BookingRepository
from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository

from services.auth_service import AuthService
from services.booking_service import BookingService
from services.room_service import RoomService

"""
dependencies for getting repository
"""
def get_room_repository(
    db = Depends(get_db)
):
    return RoomRepository(db)

def get_booking_repository(
    db = Depends(get_db)
):
    return BookingRepository(db)

def get_user_repository(
    db = Depends(get_db)
):
    return UserRepository(db)


"""
dependencies for getting services
"""
def get_email_service():
    return EmailService()

def get_auth_service(
    user_repository = Depends(get_user_repository),
    redis = Depends(get_redis_client),
    email_service = Depends(get_email_service)
):
    return AuthService(
        user_repository=user_repository,
        redis=redis,
        email_service = email_service
    )

def get_booking_service(
    booking_repository = Depends(get_booking_repository)
):
    return BookingService(
        booking_repository = booking_repository
    )

def get_room_service(
    room_repository = Depends(get_room_repository)
):
    return RoomService(
        room_repository = room_repository
    )


"""
dependency to get user_if from session_id obtained from cookie
"""
async def get_current_user(
    session_id : str | None = Cookie(default = None, alias='session_id'),
    auth_service : AuthService = Depends(get_auth_service)
):
    return await auth_service.get_current_user(session_id)