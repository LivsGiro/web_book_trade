import uuid
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from api.services.user_service import UserService
from api.schemas.user_schema import UserRequestCreate, UserResponsePublic


class UserController:
    """
    Controller for user operations.
    """
    def __init__(self, session: AsyncSession):
        self.user_service = UserService(session)
     
        
    async def create_new_user(self, data_user: UserRequestCreate) -> UserResponsePublic:
        """
        Creates a new user in the database.

        Args:
            data_user(dict): The data for the new user.

        Returns:
            User: The created user.
        """
        return await self.user_service.create_new_user(data_user)


    async def get_user_by_id(self, user_id: uuid) -> UserResponsePublic:
        """
        Retrieve a user's information by their unique identifier (UUID).

        This method queries the database for a user by their UUID and returns the user's information if found.

        Args:
            id (UUID): The unique identifier of the user to retrieve.

        Returns:
            UserResponsePublic: An instance of UserResponsePublic containing the user's data.
        """
        return await self.user_service.get_user_by_id(user_id)


    async def get_user_by_cpf(self, cpf: str) -> UserResponsePublic:
        """
        Retrieve a user's information by CPF.

        This method queries the database for a user by their CPF and returns the user's information if found.

        Args:
            cpf (str): The CPF of the user to retrieve.

        Returns:
            UserResponsePublic: An instance of UserResponsePublic containing the user's data.
        """
        return await self.user_service.get_user_by_cpf(cpf)
  
    
    async def get_user_by_email(self, email: str) -> UserResponsePublic:
        """
        Retrieve a user's information by email address.

        This method queries the database for a user by their email and returns the user's information if found.

        Args:
            email (str): The email address of the user to retrieve.

        Returns:
            UserResponsePublic: An instance of UserResponsePublic containing the user's data.
        """
        return await self.user_service.get_user_by_email(email)
    

    async def find_all_users(self, skip: int, limit: int, active: bool) -> List[UserResponsePublic]:
        """
        Retrieve all users from the service.

        Returns:
            List[UserResponsePublic]: A list of public user data.
        """       
        return await self.user_service.find_all_users(skip, limit, active)