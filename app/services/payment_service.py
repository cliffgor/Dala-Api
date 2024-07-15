# app/services/payment_service.py

from sqlalchemy.orm import Session
from app.models.booking import Booking
from fastapi import HTTPException

def process_payment(db: Session, booking_id: int):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    # Simulate payment gateway API call
    payment_data = {
        "amount": booking.price,
        "booking_id": booking.id,
        "user_id": booking.user_id
    }
    
    # In a real scenario, you would make an HTTP request to the payment gateway
    # Here, we're simulating a successful payment
    payment_response = {"status": "success", "transaction_id": f"TR-{booking.id}"}
    
    if payment_response["status"] == "success":
        # Update booking status in database
        booking.status = "paid"
        db.commit()
        return {"message": "Payment processed successfully", "transaction_id": payment_response["transaction_id"]}
    else:
        raise HTTPException(status_code=400, detail="Payment processing failed")