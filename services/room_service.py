from constants import RoomStatus
from exceptions.room_exceptions import *
from models import Room
from repositories.room_repository import RoomRepository


class RoomService:
    def __init__(self, room_repository, ):
        self.room_repository : RoomRepository = room_repository


    async def get_room_details(self, room_id) -> Room | None:
        room = await self.room_repository.get_room_details(room_id)

        if not room:
            raise CannotFetchRoomDetailsError()

        return room


    async def create_room(self, payload, user_id) -> Room | None:
        room_name = payload.room_name
        room = await self.room_repository.create_room(room_name, user_id)

        if not room:
            raise CannotCreateRoomError()

        return room


    async def edit_room_details(self, payload, user_id : str):
        room_id = payload.room_id
        new_room_name = payload.new_room_name

        room = await self.room_repository.edit_room_details(room_id, new_room_name, user_id)

        if not room:
            raise CannotEditRoomError()


    async def get_active_rooms(self) -> list[Room]:
        rooms = await self.room_repository.get_active_rooms()

        if not rooms:
            return []

        return rooms


    async def block_room(self, room_id):
        room = await self.room_repository.get_room_details(room_id)

        if not room or room.status==RoomStatus.BLOCKED.value:
            raise CannotBlockRoomError()

        room.status = RoomStatus.BLOCKED.value

        await self.room_repository.commit_and_refresh(room)


    async def unblock_room(self, room_id):
        room = await self.room_repository.get_room_details(room_id)

        if not room or room.status == RoomStatus.ACTIVE.value:
            raise CannotUnblockRoomError()

        room.status = RoomStatus.ACTIVE.value

        await self.room_repository.commit_and_refresh(room)


