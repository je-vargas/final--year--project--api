from typing import Optional
from datetime import datetime
from pydantic import (
    BaseModel, 
    validator, 
    EmailStr
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
  

class UpdateAccountSchema(BaseModel):
    id: int
    username: Optional[EmailStr] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    telephoneNumber: Optional[str] = None

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Username must not be empty")
        return username

class UpdateAccountChangesSchema(UpdateAccountSchema):
    contactDetails_id: Optional[int]



