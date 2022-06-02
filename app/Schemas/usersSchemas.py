from typing import Optional
from datetime import datetime
import re
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
    
    @validator("telephoneNumber")
    def validate_telphone(cls, telephoneNumber):
        telPattern = '^(0|\+44)(\d{10}|\d{2}\s\d{4}\s\d{4}|\s\d{4}\s\d{6})$'
        validTel = re.match(telPattern, telephoneNumber)
        if not validTel : raise ValueError("Invalid telephone number | Enter an 11 digit number beggining with 0 or +44")
        return telephoneNumber

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



