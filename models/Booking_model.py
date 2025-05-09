from utilities.database import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Float
from datetime import datetime
class Booking(Base):
    __tablename__='bookings'
    id=Column(Integer,primary_key=True,index=True)
    Check_in_date=Column(DateTime)
    Check_out_date=Column(DateTime)
    status=Column(String)
    payment_status=Column(String)
    total_price=Column(Float)
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    user_id=Column(Integer,ForeignKey('user.id'))
    room_id=Column(Integer,ForeignKey('room.id'))