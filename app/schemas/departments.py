from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import date

class DepartmentNames(str, Enum):
    engineering = "Engineering"
    hr = "Human Resources"
    finance = "Finance"
    sales = "Sales"
    marketing = "Marketing"
    operations = "Operations"

class DepartmentStatus(str, Enum):
    active = "active"
    inactive = "inactive"

   
class DepartmentBase(BaseModel):
    department_name: DepartmentNames
    supervisor_id: int
    cost_center: str
    status: DepartmentStatus
    effective_date: date

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    department_name: DepartmentNames | None = None
    supervisor_id: int | None = None
    cost_center: str | None = None
    status: DepartmentStatus | None = None
    effective_date: date | None = None

class DepartmentResponse(DepartmentBase):
    department_id: int

    model_config = {"from_attributes": True}
