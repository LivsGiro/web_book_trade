from fastapi import APIRouter, status
from typing import List, Optional
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
