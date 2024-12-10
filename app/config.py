import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("postgresql", "postgresql://postgres:planetcomm1234@localhost:5432/postgres")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "yoursecret")
JWT_ALGORITHM = "HS256"
