from fastapi  import APIRouter

router = APIRouter(
    prefix="/api/v1/rooms"
)

@router.get("/")
def get_rooms():
    pass

@router.get("/{room_id}")
def get_room_details():
    pass

@router.get("/{room_id}/availability")
def get_available_rooms():
    pass

@router.post("/")
def create_room():
    pass

@router.patch("/")
def edit_room_details():
    pass

@router.post("/block/{room_id}")
def block_room():
    pass

@router.delete("/block/{block}")
def unblock_room():
    pass