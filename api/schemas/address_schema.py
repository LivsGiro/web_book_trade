import uuid
from sqlalchemy.dialects.postgresql import UUID
from typing import Annotated
from pydantic import Field

from api.schemas.BaseSchema import BaseSchema


class AddressRequestCreate(BaseSchema):
    userId: uuid.UUID = Field(default_factory=uuid.uuid4, description="Unique identifier of the associated user.")
    country: Annotated[str, Field(..., json_schema_extra={'len': 2}, description='Two-letter country code according to ISO 3166-1 alpha-2.')]
    state: Annotated[str, Field(..., json_schema_extra={'len': 2}, description='Two-letter state code, relevant and required if applicable.')]
    city: Annotated[str, Field(..., min_length=2, max_length=50, description='Name of the city, must be between 2 and 50 characters.')]
    neighborhood: Annotated[str, Field(max_length=50, description='Name of the neighborhood, up to 50 characters.')]
    road: Annotated[str, Field(max_length=50, description='Name of the road or street, up to 50 characters.')]
    number: Annotated[str, Field(max_length=10, description='House or building number, up to 10 characters.')]
    public: Annotated[bool, Field(..., description='Flag to indicate if the address should be public. True for public, False for private.')]
    
    
class AddressResponsePublic(BaseSchema):
    userId: uuid.UUID = Field(description="Unique identifier of the associated user.")
    id: Annotated[int, Field(description="Id the address.")]
    country: Annotated[str, Field(description='Two-letter country code according to ISO 3166-1 alpha-2.')]
    state: Annotated[str, Field(description='Two-letter state code, relevant and required if applicable.')]
    city: Annotated[str, Field(description='Name of the city, must be between 2 and 50 characters.')]
    neighborhood: Annotated[str, Field(description='Name of the neighborhood, up to 50 characters.')]
    road: Annotated[str, Field(description='Name of the road or street, up to 50 characters.')]
    number: Annotated[str, Field(description='House or building number, up to 10 characters.')]
    public: Annotated[bool, Field(description='Flag to indicate if the address should be public. True for public, False for private.')]