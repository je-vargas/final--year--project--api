from typing import Optional
from datetime import datetime
from ..globalEnums import *

import re
from pydantic import (
    BaseModel, 
    validator, 
    EmailStr
    )

class NewAccountCompanySchemaIn(BaseModel):
    username: EmailStr
    password: str
    firstName: str
    lastName: str
    telephoneNumber: str
    dateCreated: datetime
    lastLogin: datetime
    companyName: str
    companyDescription: str
    industry: IdustryEnum

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
    
    @validator("firstName")
    def validate_login_firstName(cls, firstName):
        if firstName == "": 
            raise ValueError("First name must not be empty")
        return username
    
    @validator("lastName")
    def validate_login_lastName(cls, lastName):
        if lastName == "": 
            raise ValueError("Last name must not be empty")
        return username

    @validator("telephoneNumber")
    def validate_telphone(cls, telephoneNumber):
        telPattern = '^(0|\+44)(\d{10}|\d{2}\s\d{4}\s\d{4}|\s\d{4}\s\d{6})$'
        validTel = re.match(telPattern, telephoneNumber)
        if not validTel : raise ValueError("Invalid telephone number | Enter an 11 digit number beggining with 0 or +44")
        return telephoneNumber

    @validator("companyName")
    def validate_company(cls, companyName):
        if companyName == "": 
            raise ValueError(" Company name must not be empty")
        return 
    
    @validator("companyDescription")
    def validate_company_description(cls, companyDescription):
        if companyDescription == "": 
            raise ValueError(" Company Description must not be empty")
        return 
    
    @validator("industry")
    def validate_industry(cls, industry):
        if industry == "": 
            raise ValueError(" Industry must not be empty")
        return 

class NewAccountSchemaIn(BaseModel):
    username: EmailStr
    password: str
    firstName: str
    lastName: str
    telephoneNumber: str
    yearOfStudy: int
    fieldOfStudy: str
    dateCreated: datetime
    lastLogin: datetime

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Username must not be empty")
        return username
    
    @validator("firstName")
    def validate_login_firstName(cls, firstName):
        if firstName == "": 
            raise ValueError("First name must not be empty")
        return firstName
    
    @validator("lastName")
    def validate_login_lastName(cls, lastName):
        if lastName == "": 
            raise ValueError("Last name must not be empty")
        return lastName
    
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

    @validator("yearOfStudy")
    def validate_study_years(cls, yearOfStudy):
        if not yearOfStudy >= 0: 
            raise ValueError("Year of study must not greater than or equal to 0")
        return yearOfStudy

    @validator("fieldOfStudy")
    def validate_study_field(cls, fieldOfStudy):
        if fieldOfStudy == "": 
            raise ValueError("Field of study must not be empty")
        return fieldOfStudy

class NewAccountSchemaOut(BaseModel):
    id: int
    username: EmailStr
    firstName: str
    lastName: str
    telephoneNumber: str
    yearsOfStudy: int
    fieldOfStudy: str
    dateCreated: datetime

class NewAccountCompanySchemaOut(BaseModel):
    id: int
    username: EmailStr
    firstName: str
    lastName: str
    telephoneNumber: str
    accountRoleId: int
    company: str
    dateCreated: datetime

class UpdateVolunteerAccountSchema(BaseModel):
    id: int
    username: Optional[EmailStr] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    telephoneNumber: Optional[str] = None
    yearOfStudy: Optional[str] = None
    fieldOfStudy: Optional[str] = None

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Username must not be empty")
        return username
    
    @validator("firstName")
    def validate_login_firstName(cls, firstName):
        if firstName == "": 
            raise ValueError("First name must not be empty")
        return username
    
    @validator("lastName")
    def validate_login_lastName(cls, lastName):
        if lastName == "": 
            raise ValueError("Last name must not be empty")
        return username
    
    @validator("telephoneNumber")
    def validate_telphone(cls, telephoneNumber):
        telPattern = '^(0|\+44)(\d{10}|\d{2}\s\d{4}\s\d{4}|\s\d{4}\s\d{6})$'
        validTel = re.match(telPattern, telephoneNumber)
        if not validTel : raise ValueError("Invalid telephone number | Enter an 11 digit number beggining with 0 or +44")
        return telephoneNumber

    @validator("yearOfStudy")
    def validate_company(cls, yearOfStudy):
        if yearOfStudy == "": 
            raise ValueError(" Year of study must not be empty")
        return 
    
    @validator("fieldOfStudy")
    def validate_company_description(cls, fieldOfStudy):
        if fieldOfStudy == "": 
            raise ValueError(" Field of study must not be empty")
        return

class UpdateCompanyUserAccountSchema(BaseModel):
    id: int
    username: Optional[EmailStr] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    telephoneNumber: Optional[str] = None
    companyName: Optional[str] = None
    companyDescription: Optional[str] = None 
    industry: Optional[IdustryEnum] = None

    @validator("username")
    def validate_login_username(cls, username):
        if username == "": 
            raise ValueError("Username must not be empty")
        return username
    
    @validator("firstName")
    def validate_login_firstName(cls, firstName):
        if firstName == "": 
            raise ValueError("First name must not be empty")
        return username
    
    @validator("lastName")
    def validate_login_lastName(cls, lastName):
        if lastName == "": 
            raise ValueError("Last name must not be empty")
        return username
    
    @validator("telephoneNumber")
    def validate_telphone(cls, telephoneNumber):
        telPattern = '^(0|\+44)(\d{10}|\d{2}\s\d{4}\s\d{4}|\s\d{4}\s\d{6})$'
        validTel = re.match(telPattern, telephoneNumber)
        if not validTel : raise ValueError("Invalid telephone number | Enter an 11 digit number beggining with 0 or +44")
        return telephoneNumber

    @validator("companyName")
    def validate_company(cls, companyName):
        if companyName == "": 
            raise ValueError(" Company name must not be empty")
        return 
    
    @validator("companyDescription")
    def validate_company_description(cls, companyDescription):
        if companyDescription == "": 
            raise ValueError(" Company Description must not be empty")
        return 
    
    @validator("industry")
    def validate_industry(cls, industry):
        if industry == "": 
            raise ValueError(" Industry must not be empty")
        return 