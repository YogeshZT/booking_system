from exceptions.room_exceptions import CannotCreateRoomError
from models import Room
from repositories.room_repository import RoomRepository


class RoomService:
    def __init__(self, room_repository, ):
        self.room_repository : RoomRepository = room_repository

    async def get_room_details(self, room_id) -> Room:
        return await self.room_repository.get_room_details(room_id)

    async def create_room(self, payload, user_id) -> Room | None:
        room_name = payload.room_name
        room = await self.room_repository.create_room(room_name, user_id)

        if not room:
            raise CannotCreateRoomError()

        return room
