from multiprocessing.context import AuthenticationError

from utils import hash_password
from exceptions import UserAlreadyExists


class AuthService:
    def __init__(self, user_repository, redis):
        self.user_repository = user_repository
        self.redis = redis

    def login(self, payload):
        user_email = payload.email
        user_password = payload.password

    def logout(self):
        pass


    def register(self, payload):
        user_name = payload.name
        user_email = payload.email
        password = payload.password

        existing_user = self.user_repository.get_by_email(user_email)

        if existing_user:
            raise UserAlreadyExists()

        password_hash = hash_password(password)

    def verify_email(self, payload):
        pass

    def resend_verification(self, payload):
        pass

    def reset_password(self, payload):
        pass

    def forgot_password(self, payload):
        pass

    def get_current_user(self, session_id : str):
        if not session_id :
            raise AuthenticationError()

        user_id = self.redis.get(f"session{session_id}")

        if not user_id:
            raise AuthenticationError()

        return user_id