from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.services.address_service import AddressService
from api.schemas.address_schema import AddressRequestCreate, AddressResponsePublic


class AddressController:
    """
    Controller for address operations.
    """
    def __init__(self, session: AsyncSession):
        self.address_service = AddressService(session)
        
    async def create_address_user(self, address_user:AddressRequestCreate, commit=True) -> AddressResponsePublic:
        """
        Creates a new address for a user.

        Args:
            address_user (AddressRequestCreate): The address data to be added.
            commit (bool): Flag to commit the transaction. Defaults to True.

        Returns:
            AddressResponsePublic: The public view of the created address, suitable for returning in API responses.
        """
        return await self.address_service.create_address_user(address_user, commit=commit)