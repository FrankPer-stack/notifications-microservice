from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):

    # Database
    database_user: str
    database_password: str
    database_host: str
    database_port: int | str
    database_name: str
    db_pool_size = 83
    web_concurrency = 3
    pool_size = db_pool_size // web_concurrency
    
    # Twilio
    twilio_sid: str
    twilio_secret: str
    twilio_phone_number: str
    twilio_messaging_service_sid: str
    twilio_verification_sid: str
    twilio_sendgrid_api_key: str
    twilio_sendgrid_auth_sender: str
 
    # FastAPI
    host: str = "localhost"
    port: int = 8000

 
def get_settings() -> Settings:
    return Settings()