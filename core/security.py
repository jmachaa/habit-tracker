from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    print(f"Hashing password: {password}")
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    print(f"Verifying password: {plain_password} against hash: {hashed_password}")
    return pwd_context.verify(plain_password, hashed_password)

