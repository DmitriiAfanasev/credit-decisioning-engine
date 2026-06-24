import operator as op
from uuid import UUID, uuid4
from typing import Optional
from typing_extensions import Self
from pydantic import BaseModel, Field, ConfigDict, EmailStr,field_validator, model_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from .address import Address
from .reject_code import RejectCode


""" Model applicant contains filed :
    
    1) id type of integer for unical ID 
    2) First name type of string
    3) Last name type of string 
    4) Address type of other model Address 
    5) Phone number type of pydantic model
    6) Work place type of string, but a next time will be other model
    7) Income type of integer

    It is model work for first stage Pre-Scoring 

"""

class Applicant(BaseModel):

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True, validate_default=True)

    id: UUID = Field(default_factory=uuid4)
    first_name: str = Field(alias="firstName", max_length=50)
    last_name: str = Field(alias="lastName", max_length=50)
    age : int = Field(ge=18, alias="Age")
    email: Optional[EmailStr] = Field(default=None, max_length=70)
    address: Address
    id_document : Optional[int] = Field(default=None, max_length=80)
    phone: PhoneNumber = Field(alias="phone")
    work: Optional[str] = Field(default=None,max_length=200)
    income: Optional[int] = Field(default=None,ge=0)


    @field_validator('first_name', 'last_name')
    @classmethod
    def validate_name(cls, value : str):
        if len(value.strip()) < 2:
            raise ValueError(f"{RejectCode.RC_111.value} : Empty field")


    @field_validator('age')
    @classmethod
    def validate_age(cls, value : int):
        if value < 18:
            raise ValueError(f"{RejectCode.RC_002.value} : Applicant must be 18 or older")
        if value > 80:
            raise ValueError(f"{RejectCode.RC_002.value} : Age is too high")
        return value
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, value : Optional[str]): # Dispsable email address and lock russian email address
        if value is None:
            return None
        
        disposable_domains = {'tempmail', 'tmpm', 'throwaway', 'mailinator', 'yopmail'}        
        
        try:
            domain = value.split('@')[-1].lower
            if domain in disposable_domains:
                raise ValueError(f'{RejectCode.RC_500.value} : Disposable email is not allowed')
        except IndexError:
            raise ValueError(f'{RejectCode.RC_222.value} : Invalid email format')

        
    @field_validator('id_document')
    @classmethod
    def validate_document(cls, value : int) -> int:
        if value is None:
            raise ValueError(f"{RejectCode.RC_007.value} : Empty field of docs")
    
    @field_validator('work')
    @classmethod
    def validate_work(cls, value : Optional[str]) -> str:
        if value is None or str(value).strip() == "":
            raise ValueError(f"{RejectCode.RC_005.value} : Applicant doesn't work")
        return value

    @field_validator('income')
    @classmethod
    def validate_income(cls, value : Optional[int]) -> int:
        if value is None or value < 100:
            raise ValueError(f"{RejectCode.RC_004.value} : Income is too low or empty field")
        if value is None or value > 8000:
            raise ValueError(f"{RejectCode.RC_003} : Approve, but too high income. Need manuale validation. Income : {value}")
        return value
    
    @model_validator(mode='after')
    @classmethod
    def check_income_age(self) -> Self:
        if (self.age >= 18 and self.age <= 25) and self.income >= 1800:
            raise ValueError(f"{RejectCode.RC_003} : So high income and low age. Check income")
        return self
        
