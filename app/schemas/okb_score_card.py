from typing import Union, Optional
from uuid import uuid4, UUID
from pydantic import BaseModel, Field, ConfigDict, field_validator


"""
The OKB score card MOAK

Result of bureau

"""

class OkbScore(BaseModel):

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True, validate_default=True)

    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = Field(default=None, max_length=50, alias="NAME_CARD")
    first_name: Optional[str] = Field(default=None, max_length=50)
    last_name: Optional[str] = Field(default=None, max_length=50)
    id_document: Optional[Union[str, int]] = Field(alias="DOCUMNET", max_length=50)
    score: Optional[int] = Field(default=None, alias="OKB_SCORE")

    @field_validator('id_document', mode='before')
    @classmethod
    def validate_document(cls, value : Union[str, int]):
        if value is None:
            return None
        
        if isinstance(value, int):
            return str(value)
        return value


    @field_validator('score', mode='before')
    @classmethod
    def normalize_score(cls, score):
        if isinstance(score, str):
            try:
                return int(score)
            except ValueError:
                return score
        return score
