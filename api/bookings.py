from fastapi  import APIRouter, Depends

from dependencies import get_booking_service, get_current_user
from schemas.booking import CreateBookingRequest
from services.booking_service import BookingService

router = APIRouter(
    prefix="/api/v1/bookings"
)

@router.post("/")
def create_booking(
    payload : CreateBookingRequest,
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    return booking_service.create_booking(payload = payload, user_id = user_id)


@router.get("/me")
def get_user_bookings(
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    return booking_service.get_user_bookings(user_id)


@router.get("/{booking_id}")
def get_booking_details(
    booking_id :str,
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    return booking_service.get_booking_details(booking_id = booking_id, user_id = user_id)


@router.delete("/{booking_id}")
def delete_booking(
    booking_id : str,
    user_id = Depends(get_current_user),
    booking_service : BookingService = Depends(get_booking_service)
):
    return booking_service.delete_booking(booking_id = booking_id, user_id = user_id)