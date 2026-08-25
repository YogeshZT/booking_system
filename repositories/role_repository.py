from sqlalchemy import select
from sqlalchemy.orm import Session

from models.role import Role

class RoleRepository:

    def __init__(self, db: Session):
        self.db = db

    async def get_role_by_name(self, name: str) -> Role | None:

        return await self.db.scalar(
            select(Role).where(Role.name == name)
        )