from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum
from db import Base

# Use explicit pay types to ensure consistency and clarity
class PayType(str, Enum):
    hourly = "hourly"
    salary = "salary"

# Supported pay frequencies for recurring compensation record.
# This can be modified to the client's sepecific payroll schedules.
class PayFrequency(str, Enum):
    weekly = "weekly"
    biweekly = "biweekly"
    semimonthly = "semimonthly"
    monthly = "monthly"

class Compensation(Base):
    __tablename__ = "compensation"

    compensation_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    # Store high precision values to reduce rounding issues during payroll calculations.
    annual_salary = Column(Numeric(14, 6), nullable=True) 
    hourly_rate = Column(Numeric(12, 6), nullable=True)
    paycheck_amount = Column(Numeric(12, 6), nullable=True)

    pay_type = Column(SQLAlchemyEnum(PayType), nullable=False)
    pay_frequency = Column(SQLAlchemyEnum(PayFrequency), nullable=False)

    # Effective dating allows multiple compensation records per employee over time.
    effective_date = Column(Date, nullable=False) 
    