from enum import Enum


"""

Code of desicion. All code have categories

1) Approve
2) Reject of rulles
3) System 

"""
class RejectCode(Enum):

    # === Approve code ===

    RC_001 = "RC_001" # Approve
    RC_003 = "RC_003" # Manuale verification

    # === Business code ===

    RC_002 = "RC_002" # Reject of age
    RC_004 = "RC_004" # Reject of income (so loud income)
    RC_005 = "RC_005" # Reject of work (with out place of work)
    RC_006 = "RC_006" # Reject of loans (So many loans in other bank)
    RC_007 = "RC_007" # Reject of docs (Empty field of docs)
    RC_008 = "RC_008" # Reject of Income (High income and low age)

    # === Fraud reject ===

    RC_500 = "RC_500" # Reject temporal email

    # === System code ===
    RC_111 = "RC_111" # Error of validation: empty fields
    RC_222 = "RC_222" # Error of email
    RC_999 = "RC_999" # Error of validation