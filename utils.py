from argon2 import PasswordHasher
import secrets
import uuid

from argon2.exceptions import VerifyMismatchError

password_hasher = PasswordHasher()

def hash_password(password : str) ->str :
    return password_hasher.hash(password)


def generate_random_token() -> str:
    return secrets.token_urlsafe(32)


def verify_password(password: str, password_hash: str ) -> bool:
    try:
        return password_hasher.verify(password_hash, password)
    except VerifyMismatchError:
        return False


def generate_uuid() -> str:
    return str(uuid.uuid4())
