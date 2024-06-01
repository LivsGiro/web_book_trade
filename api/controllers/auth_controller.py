from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.services.auth_service import AuthService
from api.database.dependencies import get_db

class AuthController:
    def __init__(self, session: AsyncSession):
        self.auth_service = AuthService(session)
        
    async def authenticate_user(self, email: str, password: str):
        user_id = await self.auth_service.authenticate_user(email, password)
        
        return user_id