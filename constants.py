import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()

class EmailVerificationStatus(str, Enum):
    VERIFIED = "verified"
    NOT_VERIFIED = "not_verified"

class RoleId(str, Enum):
    ADMIN = "admin"
    USER = "user"

SESSION_EXPIRY_SECONDS = 60 * 60 * 24
VERIFICATION_EXPIRY_SECONDS = 60 * 30
RESET_EXPIRY_SECONDS = 60 * 30

BOOKING_SERVICE_BASE_URL = os.getenv("BOOKING_SERVICE_BASE_URL", "localhost:8000")

#SMTP config for email sending
EMAIL_SENDING_ID = os.getenv("EMAIL_SENDING_ID")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

#redis config
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

#postgres config
PG_DATABASE_URL = os.getenv("PG_DATABASE_URL")