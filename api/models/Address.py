import uuid
import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer, ForeignKey

from api.database.connection import Base

class Address(Base):
    __tablename__ = "addresses"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True, default=uuid.uuid4)
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    cep: Mapped[int] = mapped_column(Integer(), nullable=False, unique=False)
    state: Mapped[str] = mapped_column(String(2), nullable=False, index=True, unique=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    neighborhood: Mapped[str] = mapped_column(String(50), nullable=False)
    road: Mapped[str] = mapped_column(String(50), nullable=True)
    number: Mapped[str] = mapped_column(String(10), nullable=True)
    public: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=True)
    
    user = relationship("User", back_populates="addresses")
    
    