from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Enum as SQLAlchemyEnum
from app.schemas.departments import DepartmentNames
from db import Base


class Departments(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=True)
    supervisor_id = Column(Integer, nullable=False)
    cost_center = Column(String, nullable=False)
    status = Column(String, nullable=False)
    effective_date = Column(Date, nullable=False)
    department_name = Column(SQLAlchemyEnum(DepartmentNames), nullable=False)
