from fastapi  import APIRouter, Depends, Cookie, Response, Query

from dependencies import get_current_user, get_room_service, require_admin
from responses.common import SuccessResponse
from responses.models.room import RoomResponse, RoomCreateResponse, RoomDetailsResponse
from responses.room_messages import *
from schemas.room import RoomCreationRequest, RoomEditRequest
from services.room_service import RoomService

router = APIRouter(
    prefix="/api/v1/rooms"
)

@router.get("/")
async def get_rooms(
    user_id = Depends(get_current_user),
    room_service: RoomService = Depends(get_room_service)
):
    rooms = await room_service.get_active_rooms()

    response_rooms = [
        RoomResponse.model_validate(room) for room in rooms
    ]
    return SuccessResponse(
        status = True,
        message = ROOMS_FETCHED_SUCCESSFULLY_MESSAGE,
        data = {
            "rooms": response_rooms
        }
    )


@router.get("/{room_id}")
async def get_room_details(
    room_id : str,
    user_id = Depends(get_current_user),
    room_service: RoomService = Depends(get_room_service)
):
    room = await room_service.get_room_details(room_id)
    room_details_response = RoomDetailsResponse.model_validate(room)

    return SuccessResponse(
        status = True,
        message = ROOM_DETAILS_FETCHED_MESSAGE,
        data ={
            "room_details" : room_details_response
        }
    )


@router.get("/{room_id}/availability")
def get_available_rooms(
    payload : RoomEditRequest,
    user_id = Depends(get_current_user),
    room_service: RoomService = Depends(get_room_service)
):
    pass


@router.post("/")
async def create_room(
    payload: RoomCreationRequest,
    user_id = Depends(require_admin),
    room_service: RoomService = Depends(get_room_service),
):
    room = await room_service.create_room(payload, user_id)

    create_room_response = RoomCreateResponse.model_validate(room)

    return SuccessResponse(
        status = True,
        message = ROOM_CREATED_SUCCESSFULLY_MESSAGE,
        data = {
            "room_id": create_room_response
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
async def block_room(
    room_id : str,
    user_id = Depends(require_admin),
    room_service: RoomService = Depends(get_room_service)
):
    await room_service.block_room(room_id)

    return SuccessResponse(
        status=True,
        message=ROOM_BLOCKED_SUCCESSFULLY_MESSAGE,
        data={}
    )


@router.delete("/block/{room_id}")
async def unblock_room(
    room_id : str,
    user_id = Depends(require_admin),
    room_service: RoomService = Depends(get_room_service)
):
    await room_service.unblock_room(room_id)

    return SuccessResponse(
        status=True,
        message=ROOM_UNBLOCKED_SUCCESSFULLY_MESSAGE,
        data={}
    )