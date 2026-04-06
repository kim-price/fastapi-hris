from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.locations import Locations
from app.schemas.locations import LocationCreate, LocationResponse
from dependencies import get_session

router = APIRouter()

@router.get("/locations", response_model=list[LocationResponse])
def get_locations(Session = Depends(get_session)):
    locations = Session.query(Locations).all()
    return locations

@router.post("/locations", response_model=LocationResponse)
def create_location(location: LocationCreate, db: Session = Depends(get_session)):
    db_location = Locations(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@router.get("/{location_id}")
def get_location(location_id: int, db: Session = Depends(get_session)):
    location = db.query(Locations).filter(Locations.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Employee not found")
    return location

@router.put("/{location_id}", response_model=LocationResponse)
def update_location(
    location_id: int,
    new_data: LocationCreate,
    db: Session = Depends(get_session)
):
    location = db.query(Locations).filter(Locations.location_id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail=f"location {location_id} not found")
    
    location.location_name = new_data.location_name
    location.city = new_data.city
    location.country = new_data.country
    location.timezone = new_data.timezone
    location.is_active = new_data.is_active

    db.commit()
    db.refresh(location)
    
    return location