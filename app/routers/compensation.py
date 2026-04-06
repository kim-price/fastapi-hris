from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.compensation import Compensation
from app.schemas.compensation import CompensationCreate, CompensationResponse
from dependencies import get_session

router = APIRouter()

@router.get("/{employee_id}", response_model=list[CompensationResponse])
def get_compensation(employee_id: int, db: Session = Depends(get_session)):
    compensation = db.query(Compensation).filter(Compensation.employee_id == employee_id).order_by(Compensation.effective_date.desc()).all()
    if not compensation:
        raise HTTPException(status_code=404, detail="Employee not found")
    return compensation

@router.get("/{employee_id}/current", response_model=CompensationResponse)
def get_compensation(employee_id: int, db: Session = Depends(get_session)):
    compensation = db.query(Compensation).filter(Compensation.employee_id == employee_id).order_by(Compensation.effective_date.desc()).first()
    if not compensation:
        raise HTTPException(status_code=404, detail="Employee not found")
    return compensation

@router.put("/", response_model=CompensationResponse)
def update_compensation(
    new_data: CompensationCreate,
    db: Session = Depends(get_session)
):
    compensation = Compensation(**new_data.model_dump())
    if not compensation:
        raise HTTPException(status_code=404, detail=f"compensation for {employee_id} not found")
    
    db.add(compensation)
    db.commit()
    db.refresh(compensation)
    
    return compensation