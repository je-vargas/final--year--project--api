from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    database_hostname: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token: int

    class Config: 
        env_file = ".env"

settings = Settings()

