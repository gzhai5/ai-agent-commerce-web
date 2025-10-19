import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    load_dotenv()

    # set up mongodb database connection
    mongo_uri: str = os.getenv("MONGO_URI")

    # AI
    openai_api_key: str = os.getenv("OPENAI_API_KEY")

    # set up JWT
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    jwt_refresh_secret_key: str = os.getenv("JWT_REFRESH_SECRET_KEY")

    # Twilio
    twilio_account_sid: str = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token: str = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_phone_number: str = os.getenv("TWILIO_PHONE_NUMBER")
    admin_forward_phone_number: str = os.getenv("ADMIN_FORWARDING_PHONE_NUMBER")


settings = Settings()