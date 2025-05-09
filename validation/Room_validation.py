from pydantic import BaseModel
from decimal import Decimal
class RoomRequest(BaseModel):
    RoomNo:int
    RoomType:str
    RoomPrice:Decimal
    RoomAvailability:bool