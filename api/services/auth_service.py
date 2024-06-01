from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.models.User import User
from api.utils.crypt_password import has_password
from api.handlers.exceptions.auth_exceptions import InvalidCredentialsException

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def authenticate_user(self, email: str, password: str):
        """
        Authenticates a user by email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Raises:
            InvalidCredentialsException: If the credentials are invalid.
        """
        try:
            stmt = select(User).filter(User.email == email)
            result = await self.session.execute(stmt)
            user = result.scalars().first()
            
            if user:
                hashed_password = has_password(password)
                if has_password == user.password:
                    return True
            else:
                raise InvalidCredentialsException
            
        except InvalidCredentialsException:
            raise InvalidCredentialsException
        
        return user.id
        
            
