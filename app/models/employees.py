from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from app.schemas.employee import EmployeeStatus

from db import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    given_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    employment_status = Column(SQLAlchemyEnum(EmployeeStatus), nullable=False)
    job_title = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    hire_date = Column(Date, nullable=False)
    supervisor_id = Column(Integer, nullable=True)
    location_id = Column(Integer, ForeignKey("locations.location_id"))

    