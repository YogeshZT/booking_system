from abc import ABC, abstractmethod

class RoomServiceInterface(ABC):
    @abstractmethod
    async def get_room_details(self, room_id):
        pass

class AuthServiceInterface(ABC):
    pass