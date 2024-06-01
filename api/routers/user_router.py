from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, status
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.dependencies import get_db
from api.schemas.user_schema import UserRequestCreate, UserResponsePublic
from api.controllers.user_controller import UserController

router = APIRouter()

@router.post('/',
             response_model=UserResponsePublic,
             status_code=status.HTTP_201_CREATED,
             summary='Create new user',
             tags=['users'])
async def create_new_user(data_user: UserRequestCreate, 
                          db: AsyncSession = Depends(get_db)
                          ) -> UserResponsePublic:
    """ Create a new user.

    Args:
        user (UserRequest): The user data to create.
        db: Session Depends

    Returns:
        UserResponse: The created user.
        
    Raises:
        HTTPException: If the user with the given CPF or email already exists.
        HTTPException: If there is a database transaction error.
    """
    user_controller = UserController(db)
    new_user = await user_controller.create_new_user(data_user)
    return UserResponsePublic.model_validate(new_user.__dict__)
    

@router.get('/{email}/email',
            response_model=UserResponsePublic,
            status_code=status.HTTP_200_OK,
            summary='Get a user by email',
            tags=['users'])
async def get_user_by_email(email: str,
                          db: AsyncSession = Depends(get_db)
                          ) -> UserResponsePublic:
    """
    Retrieve a user by their email address.

    This endpoint fetches a user's public profile based on their email address. Email addresses are unique per user.

    Args:
        email (str): The email address of the user to retrieve.
        db (AsyncSession, optional): The database session dependency.

    Returns:
        UserResponsePublic: The user data corresponding to the provided email address.
    """
    user_controller = UserController(db)
    user = await user_controller.get_user_by_email(email)
    
    return UserResponsePublic.model_validate(user.__dict__)


@router.get('/{cpf}/cpf',
            response_model=UserResponsePublic,
            status_code=status.HTTP_200_OK,
            summary='Get a user by cpf',
            tags=['users'])
async def get_user_by_cpf(cpf: str,
                          db: AsyncSession = Depends(get_db)
                          ) -> UserResponsePublic:
    """
    Retrieve a user by their CPF.

    This endpoint fetches a user's public profile based on their CPF, a unique identifier for individuals in Brazil.

    Args:
        cpf (str): CPF of the user to retrieve.
        db (AsyncSession, optional): The database session dependency.

    Returns:
        UserResponsePublic: The user data corresponding to the provided CPF.
    """
    user_controller = UserController(db)
    user = await user_controller.get_user_by_cpf(cpf)
    
    return UserResponsePublic.model_validate(user.__dict__)


@router.get('/{id}/',
            response_model=UserResponsePublic,
            status_code=status.HTTP_200_OK,
            summary='Get a user by id',
            tags=['users'])
async def get_user_by_id(id: UUID,
                          db: AsyncSession = Depends(get_db)
                          ) -> UserResponsePublic:
    """
    Retrieve a user by their unique identifier (ID).

    This endpoint fetches a user's public profile based on their UUID. UUIDs are unique and unchangeable identifiers assigned to each user.

    Args:
        id (UUID): The unique identifier of the user to retrieve.
        db (AsyncSession, optional): The database session dependency.

    Returns:
        UserResponsePublic: The user data corresponding to the provided UUID.
    """
    user_controller = UserController(db)
    user = await user_controller.get_user_by_id(id)
    
    return UserResponsePublic.model_validate(user.__dict__)


@router.get('/', 
            response_model=List[UserResponsePublic], 
            status_code=status.HTTP_200_OK, 
            summary='Get a list of users', 
            tags=['users'])
async def find_all_users(skip: int = 0,
                         limit: int = 10,
                         active: bool = True,
                         db: AsyncSession = Depends(get_db)
                         ) -> UserResponsePublic:
    """Retrieve a list of users with pagination.

    Args:
        
        skip (int, optional): Number of records to skip for pagination.
        limit (int, optional): Maximum number of records to return.
        active (Optional[bool], optional): Filter by active users.
        user_controller (UserController, optional): The user controller. Defaults to Depends().

    Returns:
        List[UserResponsePublic]: The list of users.
        
    Raises:
        HTTPException: If no users are found.
    """
    
    user_controller = UserController(db)
    users = await user_controller.find_all_users(skip, limit, active)    
    return [UserResponsePublic.model_validate(user.__dict__) for user in users]
