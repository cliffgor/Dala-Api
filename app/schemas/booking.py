# app/schemas/booking.py

from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    user_id: int
    route_id: int
    seat_number: int
    price: float

class BookingResponse(BookingCreate):
    id: int
    booking_time: datetime
    status: str

    class Config:
        orm_mode = True