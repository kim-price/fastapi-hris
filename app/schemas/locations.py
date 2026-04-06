from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import date


class LocationBase(BaseModel):
    location_name: str
    city: str | None = None
    country: str
    timezone: str
    is_active: str

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationCreate):
    location_id: int

    model_config = {"from_attributes": True}    




