from sqlalchemy import select
from sqlalchemy.orm import joinedload

from constants import EmailVerificationStatus
from models.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    async def create_user(self, user : User):
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user


    async def get_user_by_user_id(self, user_id : str):
        user = await self.db.scalar(
            select(User).where(User.id == user_id)
        )
        return user

    async def get_user_by_email_id(self, email : str):
        user = await self.db.scalar(
            select(User).where(User.email == email)
        )
        return user


    async def update_email_verification_status(self, user_id : str, verification_status : EmailVerificationStatus):
        user = await self.get_user_by_user_id(user_id)
        user.email_verification_status = verification_status

        await self.db.commit()
        await self.db.refresh(user)

        return user


    async def get_user_password_by_email(self, email : str) -> str | None:
        user = await self.get_user_by_email_id(email)

        if user:
            return user.password_hash

        return None


    async def get_user_id_by_email(self, email : str):
        user = await self.get_user_by_email_id(email)
        if not user:
            return None

        return user.id


    async def get_user_email_verification_status(self, email : str):
        user = await self.get_user_by_email_id(email)

        if not user:
            return None

        return user.email_verification_status


    async def update_password(self, user_id : str, new_password_hash : str):
        user = await self.get_user_by_user_id(user_id)

        user.password_hash = new_password_hash
        await self.db.commit()
        await self.db.refresh(user)


    async def get_user_with_role(self, user_id: str):
        result = await self.db.execute(
            select(User)
            .options(joinedload(User.role))
            .where(User.id == user_id)
        )

        return result.scalar_one_or_none()