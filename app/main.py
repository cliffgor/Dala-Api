#app/main.py

from fastapi import FastAPI
from app.api.endpoints import bookings
from app.core import config
from app.db.session import engine
from app.models import booking

booking.Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

app.include_router(bookings.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)