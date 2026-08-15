from enum import Enum

class EmailVerificationStatus(str, Enum):
    VERIFIED = "verified"
    NOT_VERIFIED = "not_verified"

class RoleId(str, Enum):
    ADMIN = "1"
    USER = "2"

SESSION_EXPIRY_SECONDS = 60 * 60 * 24
VERIFICATION_EXPIRY_SECONDS = 60 * 30
RESET_EXPIRY_SECONDS = 60 * 30

