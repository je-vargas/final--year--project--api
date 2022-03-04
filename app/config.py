from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_hostname: str
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expiry_time: int 

    class Config: 
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()