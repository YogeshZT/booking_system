from sqlalchemy import select
from models import Room
from utils import generate_uuid


class RoomRepository:
    def __init__(self, db):
        self.db = db

    async def get_room_details(self, room_id : str) -> Room | None:
        room = await self.db.scalar(
            select(Room).where(Room.id == room_id)
        )
        return room

    async def create_room(self, room_name : str, user_id : str) -> Room | None:
        room_id = generate_uuid()
        room = Room(
            id = room_id,
            name = room_name,
            created_by = user_id,
            updated_by = user_id
        )

        self.db.add(room)
        await self.db.commit()
        await self.db.refresh(room)

        return room

    async def edit_room_details(self, room_id : str, new_room_name : str, user_id : str) -> Room | None:
        room = await self.db.scalar(
            select(Room).where(Room.id == room_id)
        )
        if not room:
            return None

        room.name = new_room_name
        room.updated_by = user_id
        await self.db.commit()
        await self.db.refresh(room)

        return room