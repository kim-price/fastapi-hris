from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum

from db import Base

class Locations(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, nullable=False)
    city = Column(String)
    country = Column(String, nullable=False)
    timezone = Column(String, nullable=False)
    is_active = Column(String, nullable=False)
    

    