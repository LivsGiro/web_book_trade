from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.services.address_service import AddressService
from api.schemas.user_schema import UserRequestCreate, UserResponsePublic


class AddressController:
    """
    Controller for user operations.
    """
    def __init__(self, session: AsyncSession):
        self.user_service = AddressService(session)
        
    async def create_address_user(self, address_user):
        pass