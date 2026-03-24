from fastapi import APIRouter
from schemas.user_schema import UserRegister
import logging

router = APIRouter()

@router.post("/register")
async def register(user: UserRegister):
    logging.info(f"Registering user: {user.email}")
    return {"message": "User registered"}