from core.config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient

setting = get_settings()

client = AsyncIOMotorClient(setting.MONGO_DB_CONNECTION_STRING)

db = client.code_go_trendz_db

job_applications = db.job_applications
contact_us_data = db.contact_us_data
