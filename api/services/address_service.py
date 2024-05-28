from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from datetime import datetime, timezone

from api.models.Address import Address
from api.schemas.address_schema import AddressRequestCreate, AddressResponsePublic
from api.handlers.exceptions.user_exceptions import UserAlreadyExistsException, UserNotFoundException
from api.handlers.exceptions.database_exceptions import DataBaseTransactionException

class AddressService:
    """
    Service layer for handling user data operations.
    """
    def __init__(self, session:AsyncSession):
        self.session = session
        
    async def create_address_user(self, address_data: AddressRequestCreate) -> AddressResponsePublic:
        data_address = address_data.model_dump()
        new_address = Address(**data_address) 
        try:
            self.session.add(new_address)          
            await self.session.commit()
            await self.session.refresh(new_address)
        except:
            await self.session.rollback()
            raise DataBaseTransactionException()
        