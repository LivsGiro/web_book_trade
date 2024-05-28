import uuid
import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer, ForeignKey

from api.database.connection import Base

class Address(Base):
    __tablename__ = "adres"

    userId: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.users_id"), primary_key=True, default=uuid.uuid4, name="users_id")
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True, name="adres_id")
    country: Mapped[str] = mapped_column(String(2), nullable=False, index=True, unique=True, name="adres_cod_country")
    state: Mapped[str] = mapped_column(String(2), nullable=False, index=True, unique=True, name="adres_cod_state")
    city: Mapped[str] = mapped_column(String(50), nullable=False, index=True, name="adres_nam_city")
    neighborhood: Mapped[str] = mapped_column(String(50), nullable=False, name="adres_nam_neighborhood")
    road: Mapped[str] = mapped_column(String(50), nullable=True, name="adres_nam_road")
    number: Mapped[str] = mapped_column(String(10), nullable=True, name="adres_cod_number")
    public: Mapped[bool] = mapped_column(Boolean(), nullable=True, default=True, name="adres_ind_public")
    
    user = relationship("User", back_populates="addresses")
    
    