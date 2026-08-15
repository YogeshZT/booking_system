from constants import EmailVerificationStatus
from models.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, user : User):
        pass

    def get_by_email(self, email : str):
        pass

    def update_email_verification_status(self, user_id : str, verification_status : EmailVerificationStatus):
        pass

    def get_user_password_by_email(self, email : str):
        pass

    def get_user_id_by_email(self, email : str):
        pass

    def get_user_email_verification_status(self, email : str):
        pass

    def update_password(self, user_id : str, new_password : str):
        pass