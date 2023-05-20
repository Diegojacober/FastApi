from pydantic import BaseSettings
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    HOST = os.getenv('DB_HOST')
    USER = os.getenv('DB_USER')
    PASS = os.getenv('DB_PASS')
    DATABASE = os.getenv('DB_NAME')
    API_V_STR: str = '/api/v1'
    DB_URL: str = f"mysql+asyncmy://{USER}:{PASS}@{HOST}/{DATABASE}"
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()