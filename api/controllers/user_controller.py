from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.services.user_service import UserService
from api.schemas.user_schema import UserRequestCreate, UserResponsePublic


class UserController:
    """
    Controller for user operations.
    """
    def __init__(self, session: AsyncSession):
        self.user_service = UserService(session)
        
    async def create_new_user(self, data_user: UserRequestCreate) -> UserResponsePublic:
        return await self.user_service.create_new_user(data_user)

    async def find_all_users(self, skip: int, limit: int, active: bool) -> List[UserResponsePublic]:
        """
        Retrieve all users from the service.

        Returns:
            List[UserResponsePublic]: A list of public user data.
        """       
        return await self.user_service.find_all_users(skip, limit, active)