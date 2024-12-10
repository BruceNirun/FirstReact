# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.utils.hashing import hash_password
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# สร้าง Pydantic Model สำหรับ Signup Request
class SignupRequest(BaseModel):
    email: EmailStr
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    # ตรวจสอบว่ามีผู้ใช้งานนี้ในระบบหรือยัง
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # สร้างผู้ใช้ใหม่
    new_user = User(
        email=request.email,
        hashed_password=hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "Signup successful"}
