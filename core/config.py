from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class get_settings(BaseSettings):
    MAX_LENGTH_FILENAME: int
    MONGO_DB_CONNECTION_STRING: str


model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
)
