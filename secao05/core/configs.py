from pydantic import BaseSettings
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    load_dotenv()
    __HOST = os.getenv('DB_HOST')
    __USER = os.getenv('DB_USER')
    __PASS = os.getenv('DB_PASS')
    __DATABASE = os.getenv('DB_NAME')
    API_V_STR: str = '/api/v1'
    DB_URL: str = f"mysql+asyncmy://{__USER}:{__PASS}@{__HOST}/{__DATABASE}"
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()