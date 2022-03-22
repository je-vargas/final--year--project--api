from typing import Optional
from datetime import datetime
from pydantic import (
    BaseModel, 
    ValidationError, 
    validator, 
    EmailStr
    )

class Credentials(BaseModel):
    username: EmailStr
    password: str

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

class UserCredentials(Credentials):
    date: Optional[datetime] = None

class UserLogInResponse(BaseModel):
    token: str

class UserIn(Credentials):
    firstname: str
    lastname: str
    createdOn: Optional[datetime] = None
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id = int
    username = EmailStr
    createdOn = datetime
    class Config:
        orm_mode = True

class Email(BaseModel):
    username: EmailStr
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class EmployerOut(BaseModel):
    id: int
    companyName: str
    companyDescription: str 

class Job(BaseModel):
    id = int
    jobDescription = str
    jobTitle = str
    numberOfPositions = int
    onGoingFill = bool
    startDate = datetime
    endDate = datetime
    applicationDeadline = datetime
class JobIn(BaseModel):
    employer_id = int
    category_id = int
class JobOut(Job):
    employer = EmployerOut
    
