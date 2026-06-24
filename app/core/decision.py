from ..schemas.reject_code import RejectCode

""" The final score store a final value of engine and decision with help inetger
    
   Example : 
    1) final score : 427
    2) List of code of reject's
    3) decision : 0, 1, or 3

    0 -> Reject
    1 -> Approve
    3 -> Manual Review

    EXPORT DATA

"""

class Decision():
    final_score: int
    list_reject : {RejectCode}
    decision: int

