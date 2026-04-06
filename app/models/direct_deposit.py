from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, Boolean
from sqlalchemy import Enum as SQLAlchemyEnum
from enum import Enum
from db import Base

# Use explicit account types to ensure consistency and clarity
class AccountType(str, Enum):
    checking = "checking"
    savings = "savings"

# Usee explicit allocation types to define how deposits are split
class DespoitType(str, Enum):
    flat = "flat"
    percent = "percent"
    remainder = "remainder"

class DirectDeposit(Base):
    __tablename__ = "direct_deposit"

    dd_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    routing_number = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    account_type = Column(SQLAlchemyEnum(AccountType), nullable=False)

    deposit_type = Column(SQLAlchemyEnum(DespoitType), nullable=False)
    deposit_value = Column(Numeric(12, 6), nullable=True)
    priority = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    