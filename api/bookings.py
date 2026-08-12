from fastapi  import APIRouter

router = APIRouter(
    prefix="/api/v1/bookings"
)

@router.post("/")
def create_booking():
    pass

@router.get("/me")
def get_user_bookings():
    pass

@router.get("/{booking_id}")
def get_booking_details():
    pass

@router.delete("/{booking_id}")
def delete_booking():
    pass