from repositories.user_repo import UserRepository
from core.security import hash_password,verify_password
from utils.security import create_access_token,create_refresh_token
from fastapi import HTTPException

class AuthService:

    def __init__(self):
        self.user_repo = UserRepository()

    async def register(self, name: str, email: str, password: str):

        # 1. Check if user already exists
        existing_user = await self.user_repo.get_user_by_email(email)

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # 2. Hash password
        # hashed_password = hash_password(password)

        # 3. Create user object
        user_data = {
            "name": name,
            "email": email,
            "password": password,
            "role": "user"
        }

        # 4. Save to DB
        await self.user_repo.create_user(user_data)

        return {"message": "User registered successfully"}
    
    async def login(self, email: str, password: str):
        # 1. Get user by email
        user = await self.user_repo.get_user_by_email(email)

        if not user:
            raise HTTPException(status_code=400, detail="Invalid email or password")

        # 2. Verify password
        # if not verify_password(password, user["password"]):
        #     raise HTTPException(status_code=400, detail="Invalid email or password")

        # 3. Create access token
        access_token = create_access_token(data={"sub": user["email"]})
        refresh_token = create_refresh_token(data={"sub": user["email"]})

        return {"message": "User logged in successfully", "access_token": access_token, "refresh_token": refresh_token, "user": {"name": user["name"], "email": user["email"], "role": user["role"]}}