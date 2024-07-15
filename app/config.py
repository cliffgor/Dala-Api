# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "Dala API"
VERSION = "1.0.0"

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/bus_booking_db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")