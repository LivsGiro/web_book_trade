from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from api.models.Address import Address
from api.schemas.address_schema import AddressRequestCreate, AddressResponsePublic
from api.handlers.exceptions.database_exceptions import DataBaseTransactionException
from sqlalchemy.exc import SQLAlchemyError

class AddressService:
    """
    Service layer for handling user data operations.
    """
    def __init__(self, session:AsyncSession):
        self.session = session
        
    async def create_address_user(self, address_data: AddressRequestCreate, commit=True) -> AddressResponsePublic:
        """
        Handles the creation of a new address entry in the database.

        Args:
            address_data (AddressRequestCreate): The data required to create a new address.
            commit (bool): If True, commits the transaction after adding the address. Defaults to True.

        Returns:
            AddressResponsePublic: Data representation of the newly created address suitable for API responses.

        Raises:
            DataBaseTransactionException: If there is an issue during the database transaction.
        """
        address_data = address_data.model_dump()                
        new_address = Address(**address_data)
        
        try:
            self.session.add(new_address)                
            if commit == True:                
                await self.session.commit()                
            await self.session.refresh(new_address)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise DataBaseTransactionException(f"Database transaction failed: {e}")
        except Exception as e:
            await self.session.rollback()
            raise DataBaseTransactionException("An unexpected error occurred. Please contact support if this continues.")

        return new_address