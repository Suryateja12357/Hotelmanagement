from fastapi import APIRouter,HTTPException
from typing import Annotated
from fastapi import Depends,Path
from sqlalchemy.orm import Session
from starlette import status
from utilities.database import SessionLocal
from models.Room_model import Room
from validation.Room_validation import RoomRequest
router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@router.get("/room",status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return db.query(Room).all()

@router.get("/room/{room_id}",status_code=status.HTTP_200_OK)
async def read_room(db:db_dependency,room_id:int=Path(gt=0)):
    room_model=db.query(Room).filter(room_id==Room.id).first()
    if room_model is not None:
        return room_model
    raise HTTPException(status_code=404,detail='room not found')

@router.post("/room",status_code=status.HTTP_201_CREATED)
async def create_room(db:db_dependency,room_request:RoomRequest):
    room_model=Room(**room_request.dict())
    db.add(room_model)
    db.commit()
    return room_model

@router.put("/room/{room_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_room(db:db_dependency,room_id:int,room_request:RoomRequest):
    room_model=db.query(Room).filter(room_id==Room.id).first()
    if room_model is None:
        raise HTTPException(status_code=404,detail='room not found')
    room_model.RoomNo=room_request.RoomNo
    room_model.RoomType=room_request.RoomType
    room_model.RoomPrice=room_request.RoomPrice
    room_model.RoomAvailability=room_request.RoomAvailability
    db.add(room_model)
    db.commit()

@router.delete("/room/{room_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_room(db:db_dependency,room_id:int):
    room_model=db.query(Room).filter(room_id==Room.id).first()
    if room_model is None:
        raise HTTPException(status_code=404,detail='room not found')
    db.query(Room).filter(room_id==Room.id).delete()
    db.commit()