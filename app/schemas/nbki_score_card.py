from uuid import UUID, uuid4
from typing import Union, Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator

"""
The NBKI score card MOAK

Result of bureau

"""

class NBKIScore(BaseModel):

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True, validate_default=True)

    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = Field(default= None, alias="NAME_CARD")
    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    id_document: Optional[Union[str, int]] = Field(default = None, alias="DOCUMENT", max_length=50)
    score: Optional[int] = Field(default=None, alias="NBKI_SCORE")

    @field_validator('id_document', mode="before")
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
