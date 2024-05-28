import uuid
import enum
from typing import Annotated
from typing import Optional
from pydantic import Field, EmailStr
from datetime import datetime

from api.schemas.BaseSchema import BaseSchema

class Gender(enum.Enum):
    Masculino = "M"
    Feminino = "F"
    Outro = "O"

class UserRequestCreate(BaseSchema):
    cpf: Annotated[str, Field(..., json_schema_extra={'len': 11}, description='CPF must be exactly 11 characters.')]
    email: Annotated[EmailStr, Field(..., max_length=45, description='Email must be at most 45 characters.')]
    name: Annotated[str, Field(..., min_length=7, max_length=100, description='Name must be between 7 and 100 characters.')]
    password: Annotated[str, Field(..., min_length=8, max_length=20, description='Password must be between 8 and 20 characters.')]
    sex: Annotated[Gender, Field(..., description="The user's gender (M for male, F for female, O for other).")]
    dateBirth: Annotated[datetime, Field(..., description="The user's date of birth.")]

    country: Annotated[str, Field(..., min_length=2, max_length=2, description='Two-letter country code according to ISO 3166-1 alpha-2.')]
    state: Annotated[str, Field(..., min_length=2, max_length=2, description='Two-letter state code, relevant and required if applicable.')]
    city: Annotated[str, Field(..., min_length=2, max_length=50, description='Name of the city, must be between 2 and 50 characters.')]
    neighborhood: Annotated[str, Field(max_length=50, description='Name of the neighborhood, up to 50 characters.')]
    road: Annotated[str, Field(max_length=50, description='Name of the road or street, up to 50 characters.')]
    number: Annotated[str, Field(max_length=10, description='House or building number, up to 10 characters.')]
    public: Annotated[bool, Field(..., description='Flag to indicate if the address should be public. True for public, False for private.')]
    
class UserResponsePublic(BaseSchema):
    id: Annotated[uuid.UUID, Field(description="The unique identifier for the user.")]
    email: Annotated[EmailStr, Field(description="The email address of the user.")]
    name: Annotated[str, Field(description="The full name of the user.")]
    sex: Annotated[str, Field(description="The gender of the user (M for male, F for female, O for other).")]
    dateBirth: Annotated[datetime, Field(description="The date of birth of the user.")]
    active: Annotated[bool, Field(description="Whether the user's account is active.")]
    dateCreated: Annotated[datetime, Field(description="The date and time when the user's account was created.")]
    dateLogin: Annotated[Optional[datetime], Field(description="The last date and time the user logged in, may be null.")]