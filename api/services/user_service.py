from typing import List
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.models.User import User
from api.controllers.address_controller import AddressController
from api.schemas.user_schema import UserRequestCreate, UserResponsePublic
from api.schemas.address_schema import AddressRequestCreate
from api.utils.crypt_password import has_password
from api.handlers.exceptions.user_exceptions import UserAlreadyExistsException, UserNotFoundException
from api.handlers.exceptions.database_exceptions import DataBaseTransactionException

class UserService:
    """
    Service layer for handling user data operations.
    """
    def __init__(self, session:AsyncSession):
        self.session = session
      
        
    async def create_new_user(self, data_user: UserRequestCreate) -> UserResponsePublic:
        """
        Creates a new user in the database.

        Args:
            data_user(dict): The data for the new user.

        Returns:
            User: The created user.

        Raises:
            UserAlreadyExistsException: If a user with the given CPF or email already exists.
            DataBaseTransactionException: If there is an error during the database transaction.
        """
        user_data = data_user.model_dump(exclude={'cep', 'number', 'public'})        
        await self.check_user_exists(user_data['cpf'], user_data['email'], user_data['whatsapp'])
        
        hashed_password = has_password(user_data['password'])
        user_data['password'] = hashed_password
        user_data['date_created'] = datetime.now(timezone.utc)
        
        try:
            new_user = User(**user_data) 
            self.session.add(new_user)
            await self.session.flush()
            address_data = data_user.model_dump(include={'cep', 'number', 'public'})
            address_data['user_id'] = new_user.id
            
            address_data = AddressRequestCreate(**address_data)
            address_controller = AddressController(self.session)         
            
            await address_controller.create_address_user(address_data, commit=True)      
            await self.session.commit()
            await self.session.refresh(new_user)
        except Exception:
            await self.session.rollback()
            raise DataBaseTransactionException(Exception)
        
        return new_user
            
        
    async def find_all_users(self, skip: int, limit: int, active: bool) -> List[UserResponsePublic]:
        """
        Fetch all users from the database.

        Returns:
            List[UserResponsePublic]: A list of user entities transformed into public response models.

        Raises:
            UserNotFoundException: If no users are found.
        """
        query = select(User)
        
        if active is False:
            query = query.where(User.active.is_(active))
            
        query = query.offset(skip).limit(limit)
        
        result = await self.session.execute(query)
        users = result.scalars().all()
        
        if not users:
            raise UserNotFoundException()
        
        return users
    
    
    async def check_user_exists(self, cpf_user: str, email_user: str, whatsapp: str) -> None:
        try:
            await self.get_user_by_cpf(cpf_user)
        except UserNotFoundException:
            pass
        else:
            raise UserAlreadyExistsException("User with this cpf already exists.")
        
        try:
            await self.get_user_by_email(email_user)
        except UserNotFoundException:
            pass
        else:
            raise UserAlreadyExistsException("User with this email already exists.")       
        
        try:
            await self.get_user_by_whatsapp(whatsapp)   
        except UserNotFoundException:
            pass
        else:
            raise UserAlreadyExistsException("User with this whastapp already exists.")       
        
    
    async def get_user_by_id(self, id_user: str) -> UserResponsePublic:
        """
        Retrieves a user by their ID.

        Args:
            ID (str): The ID of the user.

        Returns:
            User: The user with the given ID.

        Raises:
            UserNotFoundException: If no user is found with the given ID.
        """
        stmt = select(User).filter(User.id == id_user)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user
    
        
    async def get_user_by_cpf(self, cpf_user: str) -> UserResponsePublic:
        """
        Retrieves a user by their CPF.

        Args:
            cpf (str): The CPF of the user.

        Returns:
            User: The user with the given CPF.

        Raises:
            UserNotFoundException: If no user is found with the given CPF.
        """
        stmt = select(User).filter(User.cpf == cpf_user)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user
    
    
    async def get_user_by_whatsapp(self, whatsapp_user: str) -> UserResponsePublic:
        """
        Retrieves a user by their whatsapp.

        Args:
            whatsapp (str): The whatsapp of the user.

        Returns:
            User: The user with the given whatsapp.

        Raises:
            UserNotFoundException: If no user is found with the given whatsapp.
        """
        stmt = select(User).filter(User.whatsapp == whatsapp_user)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user
    
        
    async def get_user_by_email(self, email_user: str) -> UserResponsePublic:
        """
        Retrieves a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user with the given email.

        Raises:
            UserNotFoundException: If no user is found with the given email.
        """
        stmt = select(User).filter(User.email == email_user)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user
    
    