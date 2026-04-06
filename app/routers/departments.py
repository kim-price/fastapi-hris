from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.departments import Departments
from app.schemas.departments import DepartmentResponse, DepartmentCreate
from dependencies import get_session

router = APIRouter()

@router.get("/departments", response_model=list[DepartmentResponse])
def get_departments(Session = Depends(get_session)):
    departments = Session.query(Departments).all()
    return departments

@router.post("/departments", response_model=DepartmentResponse)
def create_department(department: DepartmentCreate, db: Session = Depends(get_session)):
    db_department = Departments(**department.model_dump())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

@router.get("/{department_id}")
def get_department(department_id: int, db: Session = Depends(get_session)):
    department = db.query(Departments).filter(Departments.department_id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Employee not found")
    return department

@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(
    department_id: int,
    new_data: DepartmentCreate,
    db: Session = Depends(get_session)
):
    department = db.query(Departments).filter(Departments.department_id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail=f"Department {department_id} not found")
    
    department.department_name = new_data.department_name
    department.supervisor_id = new_data.supervisor_id
    department.cost_center = new_data.cost_center
    department.status = new_data.status
    department.effective_date = new_data.effective_date

    db.commit()
    db.refresh(department)
    
    return department