from fastapi  import APIRouter, Depends, Cookie, Response, Query

from dependencies import get_current_user, get_room_service, require_admin
from responses.common import SuccessResponse
from responses.room_messages import ROOM_CREATED_SUCCESSFULLY_MESSAGE, ROOM_DETAILS_EDITED_SUCCESSFULLY_MESSAGE
from schemas.room import RoomCreationRequest, RoomEditRequest
from services.room_service import RoomService

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
async def create_room(
    payload: RoomCreationRequest,
    user_id = Depends(require_admin),
    room_service: RoomService = Depends(get_room_service),
):
    room = await room_service.create_room(payload, user_id)

    return SuccessResponse(
        status = True,
        message = ROOM_CREATED_SUCCESSFULLY_MESSAGE,
        data = {
            "room_id": room.id
        }
    )


@router.patch("/")
async def edit_room_details(
    payload : RoomEditRequest,
    user_id = Depends(require_admin),
    room_service: RoomService = Depends(get_room_service)
):
    await room_service.edit_room_details(payload,user_id)

    return SuccessResponse(
        status = True,
        message = ROOM_DETAILS_EDITED_SUCCESSFULLY_MESSAGE,
        data = {}
    )

@router.post("/block/{room_id}")
def block_room():
    pass

@router.delete("/block/{block}")
def unblock_room():
    pass