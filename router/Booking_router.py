from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends,Path,HTTPException
from sqlalchemy.orm import Session
from starlette import status
from utilities.database import SessionLocal
from models.Booking_model import Booking
from validation.Booking_validation import BookingRequest
router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@router.get('/booking',status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return db.query(Booking).all()

@router.get('/booking/{booking_id}',status_code=status.HTTP_200_OK)
async def read_booking(db:db_dependency,booking_id:int=Path(gt=0)):
    booking_model=db.query(Booking).filter(booking_id==Booking.id).first()
    if booking_model is not None:
        return booking_model
    raise HTTPException(status_code=404,detail='booking not found')

@router.post('/booking',status_code=status.HTTP_201_CREATED)
async def create_booking(db:db_dependency,booking_request:BookingRequest):
    booking_model=Booking(**booking_request.dict())
    db.add(booking_model)
    db.commit()
    return booking_model

@router.put('/booking/{booking_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_booking(db:db_dependency,booking_id:int,booking_request:BookingRequest):
    booking_model=db.query(Booking).filter(booking_id==Booking.id).first()
    if booking_model is None:
        raise HTTPException(status_code=404,detail='booking not found')
    booking_model.Check_in_date=booking_request.Check_in_date
    booking_model.Check_out_date=booking_request.Check_out_date
    booking_model.status=booking_request.status
    booking_model.payment_status=booking_request.payment_status
    booking_model.total_price=booking_request.total_price
    booking_model.created_at=booking_request.created_at
    booking_model.updated_at=booking_request.updated_at
    db.add(booking_model)
    db.commit()

@router.delete("/booking/{booking_id}")
async def delete_booking(db:db_dependency,booking_id:int):
    Booking_model=db.query(Booking).filter(booking_id==Booking.id).first()
    if Booking_model is None:
        raise HTTPException(status_code=404,detail='Booking not found')
    db.query(Booking).filter(booking_id==Booking.id).delete()
    db.commit()