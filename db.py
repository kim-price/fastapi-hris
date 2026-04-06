from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlmodel import Session
import os

# sets the echo to true in dev and false in production
# to manage logs more efficiently 
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

engine = create_engine(
    "sqlite:///hris.db",
    connect_args={"check_same_thread": False},
    echo=DEBUG 
)

Base = declarative_base()