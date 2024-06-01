from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.dependencies import get_current_user
from api.database.dependencies import get_db
from api.controllers.auth_controller import AuthController
from api.schemas.token_schema import TokenRequest, TokenResponse
from api.utils.token import create_access_token

router = APIRouter()

@router.post("/", response_model=TokenResponse, status_code=status.HTTP_200_OK, summary="User Login", tags=["auth"])
async def authenticate(data: TokenRequest, db: AsyncSession = Depends(get_db)) -> TokenResponse:
    """
    Authenticate a user and return a JWT token.

    Args:
        user (TokenRequest): The user login credentials.
        db (AsyncSession): The database session.

    Returns:
        TokenResponse: The access token and its type.

    Raises:
        InvalidCredentialsException: If the email or password is incorrect.
    """    
    auth_controller = AuthController(db)
    user_id = await auth_controller.authenticate_user(data.email, data.password)
    access_token = create_access_token(user_id=user_id)
    return TokenResponse(access_token=access_token, token_type="bearer")

@router.get("/", summary="Test Authentication", tags=["auth"])
async def test_authentication(current_user: dict = Depends(get_current_user)):
    """
    Test route to verify JWT authentication.

    Args:
        current_user (dict): The current authenticated user based on the JWT token.

    Returns:
        dict: A message confirming authentication and user information.
    """
    return {"message": "User authenticated", "user": current_user}