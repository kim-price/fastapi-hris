from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import date

class EmployeeStatus(str, Enum):
    active = "active"
    terminated = "terminated"
    leave = "leave"
    pending = "pending"
    inactive = "inactive"

class EmployeeBase(BaseModel):
    given_name: str
    family_name: str #allow mulitple words 
    middle_name: str | None = None
    email: EmailStr
    employment_status: EmployeeStatus
    department_id: int
    job_title: str
    hire_date: date
    supervisor_id: int | None = None
    location_id : int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeCreate):
    id: int

    model_config = {"from_attributes": True}