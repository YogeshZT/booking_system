from argon2 import PasswordHasher
import secrets
import uuid

password_hasher = PasswordHasher()

def hash_password(password : str) ->str :
    return password_hasher.hash(password)


def generate_random_token() -> str:
    return secrets.token_urlsafe(32)


def generate_uuid() -> str:
    return str(uuid.uuid4())
