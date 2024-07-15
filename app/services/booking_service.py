# app/services/booking_service.py

from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.schemas.booking import BookingCreate
import redis
from app.core import config

redis_client = redis.from_url(config.REDIS_URL)

def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    
    # Cache the booking details
    redis_client.setex(f"booking:{db_booking.id}", 3600, str(db_booking.id))
    
    return db_booking

def get_booking(db: Session, booking_id: int):
    # Check cache first
    cached_booking = redis_client.get(f"booking:{booking_id}")
    if cached_booking:
        return db.query(Booking).filter(Booking.id == int(cached_booking)).first()
    
    # If not in cache, query the database
    return db.query(Booking).filter(Booking.id == booking_id).first()