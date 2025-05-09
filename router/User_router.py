from fastapi import APIRouter,HTTPException
from typing import Annotated
from fastapi import Depends,Path
from sqlalchemy.orm import Session
from starlette import status
from utilities.database import SessionLocal
from models.User_model import User
from validation.User_validation import UserRequest
router=APIRouter()
#from models import User_model
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@router.get("/user",status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return db.query(User).all()

@router.get("/user/{user_id}",status_code=status.HTTP_200_OK)
async def read_user(db:db_dependency,user_id:int=Path(gt=0)):
    user_model=db.query(User).filter(user_id==User.id).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404,detail='user not found')

@router.post("/user/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,user_request:UserRequest):
    user_model=User(**user_request.dict())
    db.add(user_model)
    db.commit()
    return user_model

@router.put("/user/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db:db_dependency,user_id:int,user_request:UserRequest):
    user_model=db.query(User).filter(user_id==User.id).first()
    if user_model is None:
        raise HTTPException(status_code=404,detail='user not found')
    user_model.username=user_request.username
    user_model.name=user_request.name
    user_model.email=user_request.email
    user_model.password=user_request.password
    db.add(user_model)
    db.commit()
    
@router.delete("/user/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db:db_dependency,user_id:int):
    user_model=db.query(User).filter(user_id==User.id).first()
    if user_model is None:
        raise HTTPException(status_code=404,detail='user not found')
    db.query(User).filter(User.id==user_id).delete()
    db.commit()