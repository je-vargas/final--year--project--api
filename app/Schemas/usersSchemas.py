from typing import Optional
from datetime import datetime
from pydantic import (
    BaseModel, 
    ValidationError, 
    validator, 
    EmailStr, 
    Field
    )

class NewAccountSchemaIn(BaseModel):
    username: EmailStr
    password: str
    firstName: str
    lastName: str
    telephoneNumber: str
    dateCreated: datetime
    lastLogin: datetime

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Username must not be empty")
        return username
    
    @validator("password")
    def validate_login_password(cls, password):
        if password == "": raise ValueError("Password must not be empty")
        if len(password) < 8 : raise ValueError("Password must be 8 characters long")
        return password

class NewAccountSchemaOut(BaseModel):
    id: int
    username: EmailStr
    firstName: str
    lastName: str
    telephoneNumber: str
    accountRoleId: int
    dateCreated: datetime
  

class UpdateAccountSchemaIn(BaseModel):
    username: EmailStr
    firstName: str
    lastName: str
    telephoneNumber: str

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Username must not be empty")
        return username

    



