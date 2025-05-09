from pydantic import BaseModel
from datetime import datetime
class BookingRequest(BaseModel):
    Check_in_date:datetime
    Check_out_date:datetime
    status:str
    payment_status:str
    total_price:float
    created_at:datetime
    updated_at:datetime
    user_id:int
    room_id:int