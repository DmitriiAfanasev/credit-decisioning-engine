from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Union
from .reject_code import RejectCode

class Address(BaseModel):

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True, validate_default=True)

    city: Optional[str] = Field(default=None, max_length=100, alias="city")
    street: Optional[str] = Field(default=None, max_length=150, alias="street")
    house: Optional[Union[str, int]] = Field(default=None, alias="house")
    flat : Optional[Union[str, int]] = Field(default=None, alias="apartment")
    postcode: Optional[Union[str, int]] = Field(default=None, alias="postal_code")

    @field_validator('city', 'street')
    @classmethod
    def validate_fields(cls, value : str):
        if value is None or str.strip(value) == "":
            raise ValueError(f"{RejectCode.RC_003} : empty field city or street. Manuale validate")
        
