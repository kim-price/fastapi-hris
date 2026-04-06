from pydantic import BaseModel
from enum import Enum
from decimal import Decimal

# Use explicit account types to ensure consistency and clarity
class AccountType(str, Enum):
    checking = "checking"
    savings = "savings"

# Usee explicit allocation types to define how deposits are split
class DespositType(str, Enum):
    flat = "flat"
    percent = "percent"
    remainder = "remainder"
   
class DirectDepositBase(BaseModel):
    employee_id: int
    routing_number: str
    account_number: str
    account_type: AccountType
    deposit_type: DespositType
    deposit_value: Decimal | None = None
    priority: int
    is_active: bool

class DirectDepositCreate(DirectDepositBase):
    pass

class DirectDepositResponse(DirectDepositBase):
    dd_id: int

    model_config = {"from_attributes": True}

    