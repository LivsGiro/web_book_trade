import uuid
from sqlalchemy.dialects.postgresql import UUID
from typing import Annotated, Optional
from pydantic import Field

from api.schemas.base_schema import BaseSchema


class AddressRequestCreate(BaseSchema):
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, description="Unique identifier of the associated user.")
    cep: Annotated[int, Field(..., json_schema_extra={'length': 8}, description='CEP must be either 12345678 format.')]
    number: Optional[Annotated[str, Field(max_length=10, description='House or building number, up to 10 characters.')]]
    public: Annotated[bool, Field(default=True, description='Flag to indicate if the address should be public. True for public, False for private.')]
    
    
class AddressResponsePublic(BaseSchema):
    user_id: uuid.UUID = Field(description="Unique identifier of the associated user.")
    id: Annotated[int, Field(description="Id the address.")]
    cep: Annotated[int, Field(description='EP must be either 12345678 format.')]
    state: Annotated[str, Field(description='Two-letter state code, relevant and required if applicable.')]
    city: Annotated[str, Field(description='Name of the city, must be between 2 and 50 characters.')]
    neighborhood: Annotated[str, Field(description='Name of the neighborhood, up to 50 characters.')]
    road: Annotated[str, Field(description='Name of the road or street, up to 50 characters.')]
    number: Annotated[str, Field(description='House or building number, up to 10 characters.')]
    public: Annotated[bool, Field(description='Flag to indicate if the address should be public. True for public, False for private.')]