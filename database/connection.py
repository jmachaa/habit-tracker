from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://thomasempogesinfotech_db_user:Thomaspy%401@cluster0.kqelzmy.mongodb.net/habit_tracker"

client = AsyncIOMotorClient(MONGO_URL)

database = client.habit_tracker

users_collection = database.get_collection("users")
habits_collection = database.get_collection("habits")