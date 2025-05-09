from utilities.database import Base
from sqlalchemy import Column,String,Integer,DECIMAL,Boolean
class Room(Base):
    __tablename__='room'
    id=Column(Integer,primary_key=True,index=True)
    RoomNo=Column(Integer)
    RoomType=Column(String)
    RoomPrice=Column(DECIMAL)
    RoomAvailability=Column(Boolean,default=True)