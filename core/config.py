from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class get_settings(BaseSettings):
    MAX_LENGTH_FILENAME: int
    MONGO_DB_CONNECTION_STRING: str

    # email Sending Credentials:-
    EMAIL_PORT: int
    EMAIL_HOST: str
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str

    SEND_MAIL_TO: str


model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
)
