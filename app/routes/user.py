from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.utils.hashing import verify_password, hash_password
from app.utils.jwt import create_access_token
from app.models.user import User
from datetime import timedelta
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

class LoginRequest(BaseModel):
    email: str
    password: str

class SignupRequest(BaseModel):
    email: str
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=request.email,
        hashed_password=hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "Signup successful"}

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, 
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
