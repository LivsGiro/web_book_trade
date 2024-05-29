from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from datetime import datetime, timezone
from uuid import UUID

from api.models.Address import Address
from api.schemas.address_schema import AddressRequestCreate, AddressResponsePublic
from api.handlers.exceptions.user_exceptions import UserAlreadyExistsException, UserNotFoundException
from api.handlers.exceptions.database_exceptions import DataBaseTransactionException
from sqlalchemy.exc import SQLAlchemyError

class AddressService:
    """
    Service layer for handling user data operations.
    """
    def __init__(self, session:AsyncSession):
        self.session = session
        
    async def create_address_user(self, address_data: AddressRequestCreate) -> AddressResponsePublic:
        try:
            if address_data is dict:
                address_data = address_data.model_dump()
                
            new_address = Address(**address_data)
            self.session.add(new_address)
            await self.session.commit()
            await self.session.refresh(new_address)
            return new_address
        except SQLAlchemyError as e:
            await self.session.rollback()
            print(f"SQLAlchemy Error: {e}")
            raise DataBaseTransactionException(f"Database transaction failed: {e}")
        except Exception as e:
            await self.session.rollback()
            print(f"Unexpected error: {e}")
            raise

        