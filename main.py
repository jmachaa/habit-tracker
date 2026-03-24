from fastapi import FastAPI
from routes import auth_routes
from api.routes import auth

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Habit Tracker API is running!"}

app.include_router(auth_routes.router)
app.include_router(auth.router)
