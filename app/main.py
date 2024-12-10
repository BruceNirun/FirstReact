from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user import router as user_router 
from app.routes.auth import router as auth_router

app = FastAPI()

# ตั้งค่า CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ต้นทางที่อนุญาต
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุกเมธอด เช่น POST, GET, PUT, DELETE
    allow_headers=["*"],  # อนุญาตทุก Header
)

# เพิ่ม Router จาก user.py
app.include_router(user_router)
app.include_router(auth_router) 

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with CORS enabled!"}