from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .role import Role
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

    role: Mapped["Role"] = relationship(
        "Role",
        back_populates="users",
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
        SQLEnum(
            EmailVerificationStatus,
            name="email_verification_status",
            values_callable=lambda enum: [e.value for e in enum],
        ),
        nullable=False,
        default=EmailVerificationStatus.NOT_VERIFIED,
    )