from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.employees import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from dependencies import get_session

router = APIRouter()

@router.get("/", response_model=list[EmployeeResponse])
def get_employee(Session = Depends(get_session)):
    employees = Session.query(Employee).all()
    return employees

@router.post("/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_session)):
    db_employee = Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_session)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    new_data: EmployeeCreate,
    db: Session = Depends(get_session)
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    employee.given_name = new_data.given_name
    employee.family_name = new_data.family_name
    employee.middle_name = new_data.middle_name
    employee.email = new_data.email
    employee.employment_status = new_data.employment_status
    employee.department_id = new_data.department_id
    employee.job_title = new_data.job_title
    employee.hire_date = new_data.hire_date
    employee.supervisor_id = new_data.supervisor_id
    employee.location_id = new_data.location_id

    db.commit()
    db.refresh(employee)
    
    return employee

@router.delete("/{employee_id}", status_code=204)
def delete_employee(employee_id: int, db: Session = Depends(get_session)) -> None:
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")
    return employee
