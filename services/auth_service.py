from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from utils import hash_password, generate_random_token, generate_uuid, verify_password
from exceptions.auth_exceptions import *
from models.user import User
from constants import EmailVerificationStatus, RoleId, SESSION_EXPIRY_SECONDS, VERIFICATION_EXPIRY_SECONDS, RESET_EXPIRY_SECONDS


class AuthService:
    def __init__(self, user_repository, role_repository, redis, email_service):
        self.user_repository : UserRepository = user_repository
        self.role_repository : RoleRepository = role_repository
        self.redis = redis
        self.email_service = email_service


    async def login(self, payload) -> str:
        user_email = payload.email
        user_password = payload.password

        hashed_password = await self.user_repository.get_user_password_by_email(user_email)

        if not hashed_password:
            raise AuthenticationError()

        if not verify_password(user_password, hashed_password):
            raise WrongPasswordError()

        session_id = generate_uuid()
        user_id = await self.user_repository.get_user_id_by_email(user_email)
        await self.redis.set(
            f"session{session_id}",
            user_id,
            ex = SESSION_EXPIRY_SECONDS
        )

        return session_id


    async def logout(self, session_id: str):
        await self.redis.delete(f"session{session_id}")


    async def register(self, payload):
        name = payload.name
        email = payload.email
        password = payload.password

        user_id = await self.user_repository.get_user_id_by_email(email)
        if user_id:
            raise UserAlreadyExists()

        verification_token = generate_random_token()
        user_id = generate_uuid()
        await self.redis.set(
            f"verify:{verification_token}",
            user_id,
            ex = VERIFICATION_EXPIRY_SECONDS
        )

        password_hash = hash_password(password)
        role = await self.role_repository.get_role_by_name(RoleId.USER.value)
        user = User(
            id = user_id,
            name=name,
            email = email,
            password_hash = password_hash,
            role_id = role.id,
        )
        await self.user_repository.create_user(user)

        await self.email_service.send_verification_email(
            receiver=email,
            verification_token=verification_token
        )


    async def verify_email(self, verification_token):
        key = f"verify:{verification_token}"

        user_id = await self.redis.get(key)
        if user_id is None:
            raise EmailVerificationError()

        user_id = user_id.decode("utf-8")

        await self.user_repository.update_email_verification_status(user_id, EmailVerificationStatus.VERIFIED.value)
        await self.redis.delete(key)


    async def resend_verification(self, payload):
        email = payload.email
        verification_status = await self.user_repository.get_user_email_verification_status(email)

        if not verification_status:
            raise AuthenticationError()

        if verification_status == EmailVerificationStatus.VERIFIED.value:
            raise AlreadyVerifiedError()

        verification_token = generate_random_token()
        user_id = await self.user_repository.get_user_id_by_email(email)

        await self.redis.set(
            f"verify:{verification_token}",
            user_id,
            ex = VERIFICATION_EXPIRY_SECONDS
        )

        await self.email_service.send_verification_email(
            receiver=email,
            verification_token=verification_token
        )


    async def forgot_password(self, payload):
        email = payload.email
        user_id = await self.user_repository.get_user_id_by_email(email)

        if not user_id:
            return

        reset_token = generate_random_token()
        key = f"reset_password:{reset_token}"
        await self.redis.set(
            key,
            user_id,
            ex = RESET_EXPIRY_SECONDS
        )

        await self.email_service.send_reset_password_email(
            receiver=email,
            reset_token=reset_token
        )


    async def reset_password(self, payload):
        reset_token = payload.reset_token
        key = f"reset_password:{reset_token}"

        user_id = await self.redis.get(key)
        if not user_id:
            raise AuthenticationError()

        user_id = user_id.decode("utf-8")
        new_password = payload.new_password
        new_password_hash = hash_password(new_password)

        await self.user_repository.update_password(user_id, new_password_hash)
        await self.redis.delete(key)


    async def get_current_user(self, session_id : str | None = None) -> str:
        if not session_id :
            raise AuthenticationError()

        user_id = await self.redis.get(f"session{session_id}")
        if not user_id:
            raise AuthenticationError()
        user_id = user_id.decode('utf-8')
        return user_id

    async def get_admin(self, user_id):
        user = await self.user_repository.get_user_with_role(user_id)

        if not user:
            raise AuthorizationError()

        if user.role.name != RoleId.ADMIN.value:
            raise AuthorizationError()

        return user.id




