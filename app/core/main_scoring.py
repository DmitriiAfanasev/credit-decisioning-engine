from uuid import UUID
from ..schemas.eqiufax_score_card import EquifaxScore
from ..schemas.nbki_score_card import NBKIScore
from ..schemas.okb_score_card import OkbScore

"""

--- Business Logic of Main Scoring --- 


"""

class MainScoring:
    
    alg_id : UUID = 102
    
    def __init__(self, id : UUID, 
                 nbki : NBKIScore, 
                 okb : OkbScore, 
                 equifax : EquifaxScore
        ):
        self.id = id
        self.nbki = nbki
        self.okb = okb
        self.equifax = equifax