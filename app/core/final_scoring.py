from uuid import UUID
from ..schemas.ml_score_card import MlScore
class FinalScoring:
    alg_id : UUID = 103
    def __init__(self, ml_score : MlScore):
        pass