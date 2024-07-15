# app/api/endpoints/bookings.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import dependencies
from app.schemas.booking import BookingCreate, BookingResponse
from app.services import booking_service, payment_service

router = APIRouter()

@router.post("/bookings/", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(dependencies.get_db)):
    return booking_service.create_booking(db, booking)

@router.get("/bookings/{booking_id}", response_model=BookingResponse)
def read_booking(booking_id: int, db: Session = Depends(dependencies.get_db)):
    booking = booking_service.get_booking(db, booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.post("/process_payment/{booking_id}")
def process_payment(booking_id: int, db: Session = Depends(dependencies.get_db)):
    return payment_service.process_payment(db, booking_id)