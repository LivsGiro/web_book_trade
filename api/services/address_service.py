from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from datetime import datetime, timezone

from api.models.User import User
from api.schemas.user_schema import UserRequestCreate, UserResponsePublic
from api.handlers.exceptions.user_exceptions import UserAlreadyExistsException, UserNotFoundException
from api.handlers.exceptions.database_exceptions import DataBaseTransactionException

class AddressService:
    """
    Service layer for handling user data operations.
    """
    def __init__(self, session:AsyncSession):
        self.session = session
        
    async def create_address_user(self, address_data):
        data_address = address_data.model_dump()