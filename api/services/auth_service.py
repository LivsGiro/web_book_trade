from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.models.User import User
from api.utils.crypt_password import verify_password
from api.handlers.exceptions.auth_exceptions import InvalidCredentialsException
from api.handlers.exceptions.database_exceptions import DataBaseTransactionException

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
            
            if user and verify_password(password, user.password):               
                date_time = datetime.now()
                try:
                    user.date_login = date_time
                    await self.session.commit()
                    await self.session.refresh(user)
                except Exception:
                    await self.session.rollback()
                    raise DataBaseTransactionException(Exception)
                return user.id
            else:
                raise InvalidCredentialsException
            
        except InvalidCredentialsException:
            raise InvalidCredentialsException
        
            
