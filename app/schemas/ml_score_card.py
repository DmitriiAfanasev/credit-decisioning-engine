from uuid import UUID, uuid4
from typing import Union, Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator
from pydantic.dataclasses import dataclass


class MlScore(BaseModel):

    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True, validate_default=True)

    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = Field(default=None, alias="name_card")
    score_okb: Optional[int] = Field(default=None)
    score_nbki: Optional[int] = Field(default=None)
    score_eqiufax: Optional[int] = Field(default=None)
    score: Optional[int] = Field(default=None, alias="ML_SCORE")

    @field_validator('score', 'score_okb', 'score_nbki', 'score_eqiufax',mode='before')
    @classmethod
    def normalize_score(cls, score):
        if isinstance(score, str):
            try:
                return int(score)
            except ValueError:
                return score
        return score