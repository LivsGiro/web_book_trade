import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Date, DateTime, func
from datetime import datetime, date

from api.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, index=True, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(45), nullable=False, index=True, unique=True)
    whatsapp: Mapped[str] = mapped_column(String(14), nullable=True, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    date_birth: Mapped[date] = mapped_column(Date, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    notification_email: Mapped[bool] = mapped_column(Boolean, default=True)
    notification_whats: Mapped[bool] = mapped_column(Boolean, default=True)
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=func.now())
    date_login: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")