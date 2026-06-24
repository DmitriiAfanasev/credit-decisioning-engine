from uuid import UUID
from dataclasses import dataclass

from ..schemas.applicant import Applicant
from ..schemas.reject_code import RejectCode
from .decision import Decision

"""

--- Business Logic of Pre Scoring --- 
    
    Every application create a new Object with uniqle ID
    Pre-Scoring has ID of algrithm it's 101. In data base we can index woth this ID
    
"""

@dataclass
class PreScoring:
    __alg_id = 101
    __id : UUID
    applicant : Applicant
    _decision : Decision

    @staticmethod
    def RC_008(age : int, income : int):
        if (age >= 18 and age < 25) and income > 2500:
            return RejectCode.RC_008.value
        
        if age >= 25 and income >= 2500:
            return RejectCode.RC_003.value
        
    def run(self) -> Decision:
        result = self.RC_008()

        if result:
            self._decision
        
        return self._decision

    
        
    
