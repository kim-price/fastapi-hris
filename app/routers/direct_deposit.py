from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.direct_deposit import DirectDeposit
from app.schemas.direct_deposit import DirectDepositCreate, DirectDepositResponse
from dependencies import get_session

router = APIRouter()

@router.get("/{employee_id}", response_model=list[DirectDepositResponse])
def get_direct_deposit(employee_id: int, db: Session = Depends(get_session)):
    direct_deposit = db.query(DirectDeposit)\
    .filter(DirectDeposit.employee_id == employee_id)\
    .order_by(DirectDeposit.priority.asc())\
    .all()
    if not direct_deposit:
        raise HTTPException(status_code=404, detail=f"Direct Deposit information for {employee_id} not found")
    return direct_deposit

@router.post("/", response_model=DirectDepositResponse)
def create_direct_deposit(direct_deposit: DirectDepositCreate, db: Session = Depends(get_session)):
    db_direct_deposit = DirectDeposit(**direct_deposit.model_dump())
    db.add(db_direct_deposit)
    db.commit()
    db.refresh(db_direct_deposit)
    return db_direct_deposit

@router.put("/{dd_id}", response_model=DirectDepositResponse)
def update_direct_deposit(
    dd_id: int,
    new_data: DirectDepositCreate,
    db: Session = Depends(get_session)
):
    direct_deposit = db.query(DirectDeposit).filter(DirectDeposit.dd_id == dd_id).first()
    if not direct_deposit:
        raise HTTPException(status_code=404, detail=f"Direct Deposit {dd_id} not found")
    
    direct_deposit.routing_number = new_data.routing_number
    direct_deposit.account_number = new_data.account_number
    direct_deposit.account_type = new_data.account_type
    direct_deposit.deposit_type = new_data.deposit_type
    direct_deposit.deposit_value = new_data.deposit_value
    direct_deposit.priority = new_data.priority
    direct_deposit.is_active = new_data.is_active

    db.commit()
    db.refresh(direct_deposit)
    
    return direct_deposit

@router.delete("/{dd_id}", status_code=204)
def delete_direct_deposit(dd_id: int, db: Session = Depends(get_session)) -> None:
    direct_deposit = db.query(DirectDeposit).filter(DirectDeposit.dd_id == dd_id).first()
    if direct_deposit:
        db.delete(direct_deposit)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Direct Deposit {dd_id} not found")
