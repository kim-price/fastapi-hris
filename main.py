from fastapi import FastAPI
from db import Base, engine
from app.routers import employees, departments, locations, compensation, direct_deposit


Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRIS API")

app.include_router(employees.router, prefix="/api/employees", tags=["Employees"])
app.include_router(departments.router, prefix="/api/departments", tags=["Departments"])
app.include_router(locations.router, prefix="/api/locations", tags=["Locations"])
app.include_router(compensation.router, prefix="/api/compensation", tags=["Compensation"])
app.include_router(direct_deposit.router, prefix="/api/direct_deposit", tags=["Direct Deposit"])


