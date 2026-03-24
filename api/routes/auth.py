from fastapi import APIRouter
from schemas.user_schema import UserRegister, UserLogin
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: UserRegister):

    auth_service = AuthService()

    return await auth_service.register(
        user.name,
        user.email,
        user.password
    )

@router.post("/login")
async def login(user: UserLogin):

    auth_service = AuthService()

    return await auth_service.login(user.email, user.password)
    