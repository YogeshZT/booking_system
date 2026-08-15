from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

from constants import EmailVerificationStatus

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="active",
    )

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    email_verification_status: Mapped[EmailVerificationStatus] = mapped_column(
        SQLEnum(EmailVerificationStatus),
        nullable=False,
        default=EmailVerificationStatus.NOT_VERIFIED,
    )
