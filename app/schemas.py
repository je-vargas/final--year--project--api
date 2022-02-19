from pydantic import BaseModel, ValidationError, validator
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserIn(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str
    createdOn: Optional[datetime] = None
    class Config:
        orm_mode = True

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Usernmame must not be empty")

        return username
    
    @validator("password")
    def validate_login_password(cls, password):
        if password == "": raise ValueError("Usernmame must not be empty")
        if len(password) < 8 : raise ValueError("Password must be 8 characters long")
        return password

class UserOut(BaseModel):
    id = int
    username = EmailStr
    createdOn = datetime
    class Config:
        orm_mode = True

class Email(BaseModel):
    username: str
    class Config:
        orm_mode = True