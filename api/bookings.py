from fastapi  import APIRouter, Depends

from dependencies import get_booking_service, get_current_user, require_admin
from responses.booking_messages import *
from responses.common import SuccessResponse
from responses.models.booking import BookingCreateResponse, BookingsFetchResponse
from schemas.booking import CreateBookingRequest
from services.booking_service import BookingService

router = APIRouter(
    prefix="/api/v1/bookings"
)

@router.post("/")
async def create_booking(
    payload : CreateBookingRequest,
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    booking = await booking_service.create_booking(payload = payload, user_id = user_id)
    booking_create_response = BookingCreateResponse.model_validate(booking)

    return SuccessResponse(
        status = True,
        message = BOOKING_CREATED_MESSAGE,
        data = {
            "booking_id": booking_create_response
        }
    )


@router.get("/me")
async def get_user_bookings(
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    bookings = await booking_service.get_user_bookings(user_id)

    response_bookings = [
        BookingCreateResponse.model_validate(booking) for booking in bookings
    ]

    return SuccessResponse(
        status = True,
        message = USER_BOOKINGS_FETCHED_SUCCESSFULLY_MESSAGE,
        data = {
            "bookings" : response_bookings
        }
    )


@router.get("/{booking_id}")
async def get_booking_details(
    booking_id :str,
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    booking = await booking_service.get_booking_details(booking_id = booking_id, user_id = user_id)
    response_booking = BookingsFetchResponse.model_validate(booking)

    return SuccessResponse(
        status=True,
        message=BOOKING_DETAILS_FETCHED_SUCCESSFULLY_MESSAGE,
        data={
            "booking": response_booking
        }
    )


@router.delete("/{booking_id}")
async def delete_booking(
    booking_id : str,
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    await booking_service.delete_booking(booking_id = booking_id, user_id = user_id)

    return SuccessResponse(
        status=True,
        message=USER_BOOKING_DELETED_SUCCESSFULLY_MESSAGE,
        data={}
    )
