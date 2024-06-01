import uuid
from typing import Annotated, Optional
from typing import Optional
from pydantic import Field, EmailStr
from datetime import datetime, date

from api.schemas.base_schema import BaseSchema

class UserRequestCreate(BaseSchema):
    cpf: Annotated[str, Field(..., min_length=11, max_length=11, description='CPF must be exactly 11 characters.')]
    email: Annotated[EmailStr, Field(..., max_length=45, description='Email must be at most 45 characters.')]
    whatsapp: Optional[Annotated[str, Field(max_length=14, description='WhatsApp number with a maximum of 14 characters')]] = None
    name: Annotated[str, Field(..., min_length=7, max_length=100, description='Name must be between 7 and 100 characters.')]
    password: Annotated[str, Field(..., min_length=8, max_length=20, description='Password must be between 8 and 20 characters.')]
    sex: Annotated[str, Field(..., min_length=1, max_length=1, description="The user's gender (M for male, F for female, O for other).")]
    date_birth: Annotated[date, Field(..., description="The user's date of birth.")]
    notification_email: Optional[Annotated[bool, Field(default=True, description='Flag to indicate if the notification by email')]]
    notification_whats: Optional[Annotated[bool, Field(default=True, description='Flag to indicate if the notification by whatsapp')]]

    cep: Annotated[int, Field(..., json_schema_extra={'length': 8}, description='CEP must be either 12345678 format.')]
    number: Optional[Annotated[str, Field(max_length=10, description='House or building number, up to 10 characters.')]] = None
    public: Annotated[bool, Field(default=True, description='Flag to indicate if the address should be public. True for public, False for private.')]
    
    
    
class UserResponsePublic(BaseSchema):
    id: Annotated[uuid.UUID, Field(description="The unique identifier for the user.")]
    email: Annotated[EmailStr, Field(description="The email address of the user.")]
    name: Annotated[str, Field(description="The full name of the user.")]
    sex: Annotated[str, Field(description="The gender of the user (M for male, F for female, O for other).")]
    date_birth: Annotated[datetime, Field(description="The date of birth of the user.")]
    active: Annotated[bool, Field(description="Whether the user's account is active.")]
    date_created: Annotated[datetime, Field(description="The date and time when the user's account was created.")]
    date_login: Annotated[Optional[datetime], Field(description="The last date and time the user logged in, may be null.")]