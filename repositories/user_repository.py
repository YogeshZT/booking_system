from sqlalchemy import select

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

    async def update_email_verification_status(self, user_id : str, verification_status : EmailVerificationStatus):
        user = await self.db.scalar(
            select(User).where(User.id == user_id)
        )
        user.email_verification_status = verification_status

        await self.db.commit()
        await self.db.refresh(user)

        return user


    def get_user_password_by_email(self, email : str):
        pass

    async def get_user_id_by_email(self, email : str):
        user = await self.db.scalar(
            select(User).where(User.email == email)
        )
        if not user:
            return None

        return user.id

    async def get_user_email_verification_status(self, email : str):
        user = await self.db.scalar(
            select(User).where(User.email == email)
        )
        if not user:
            return None

        return user.email_verification_status


    async def update_password(self, user_id : str, new_password_hash : str):
        user = await self.db.scalar(
            select(User).where(User.id == user_id)
        )

        user.password_hash = new_password_hash
        await self.db.commit()
        await self.db.refresh(user)
