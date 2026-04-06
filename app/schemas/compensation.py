from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import date
from decimal import Decimal

class PayType(str, Enum):
    hourly = "hourly"
    salary = "salary"

class PayFrequency(str, Enum):
    weekly = "weekly"
    biweekly = "biweekly"
    semimonthly = "semimonthly"
    monthly = "monthly"


class CompensationBase(BaseModel):
    employee_id: int
    annual_salary: Decimal | None = None
    hourly_rate: Decimal | None = None
    paycheck_amount: Decimal | None = None
    pay_type: PayType
    pay_frequency: PayFrequency
    effective_date: date

class CompensationCreate(CompensationBase):
    pass

class CompensationResponse(CompensationCreate):
    # compensation_id: int

    model_config = {"from_attributes": True}    




