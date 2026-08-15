import os
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

BOOKING_SERVICE_BASE_URL = os.getenv("BOOKING_SERVICE_BASE_URL", "localhost:8000")

EMAIL_SENDING_ID = os.getenv("EMAIL_SENDING_ID")