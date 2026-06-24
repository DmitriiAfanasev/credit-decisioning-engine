from uuid import UUID, uuid4
from typing import Optional, Union
from pydantic import BaseModel, Field, ConfigDict, field_validator

"""
The Eqiufax score card MOAK

Result of bureau

"""
class EquifaxScore(BaseModel):

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True, validate_default=True)

    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = Field(default=None, max_length=100, alias="NAME_CARD")
    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    id_document: Optional[Union[int, str]] = Field(default=None, alias="DOCUMENT",max_length=50)
    score: Optional[int] = Field(default=None, alias="EQ_SCORE")

    @field_validator('id_document', mode='before')
    @classmethod
    def validate_document(cls, value : Union[str, int]) -> str:
        if value is None:
            return None
        
        if isinstance(value, int):
            return str(value)
        return value

    @field_validator("score", mode="before")
    @classmethod
    def normalize_score(cls, score):
        if score is None:
            return None
        if isinstance(score, str):
            try:
                return int(score)
            except ValueError:
                return score
        return score