# app/models/booking.py

from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    route_id = Column(Integer, index=True)
    seat_number = Column(Integer)
    price = Column(Float)
    booking_time = Column(DateTime)
    status = Column(String, default="pending")