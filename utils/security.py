from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(hours=2)

    data.update({"exp": expire})

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token

def create_refresh_token(data: dict):

    expire = datetime.utcnow() + timedelta(days=15)

    data.update({"exp": expire, "type": "refresh"})

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)