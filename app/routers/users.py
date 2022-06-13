from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from ..import models, utils, schemas, outh2
from ..Schemas.usersSchemas import *
from ..Repositories import userRepository
from enum import Enum

router = APIRouter(
    prefix="/users",
    tags=["Users"]
    )

class AccountRoles(Enum):
    """Docstring for MyEnum."""
    volunteer = 1
    employer = 2
    recruiter = 3


#: --------- CREATE ---------
@router.post("/new/volunteer", response_model=NewAccountSchemaOut, status_code=status.HTTP_201_CREATED)
def new_volunteer(user: NewAccountSchemaIn, db: Session = Depends(get_db)):

    role = AccountRoles.volunteer

    user_exists = userRepository.get_user_by_username(user.username, db)
    unique_tel = userRepository.check_unique_telephone(user.telephoneNumber, db)
    if user_exists.first() != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists")
    if unique_tel.first() != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Telephone number: {user.telephoneNumber} already exists")

    user.password = utils.hash_pwd(user.password)
    new_user = models.UserAccount(
        username=user.username, 
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephoneNumber=user.telephoneNumber,
        dateCreated=user.dateCreated, 
        lastLogin=user.lastLogin
        )
    
    new_user = userRepository.create_new_user(new_user, db)

    account_role = models.AccountRoles(userAccountId = new_user.id, roles_id = role.value)

    account_role = userRepository.create_account_role(account_role, db)

    user_skills = models.VolunteerSkills(
        userAccount_id = new_user.id,
        yearOfStudy = user.yearOfStudy,
        fieldOfStudy = user.fieldOfStudy
    )
 
    new_user_skills = userRepository.create_user_skills_link(user_skills, db)

    user_out = NewAccountSchemaOut(
        id=new_user.id,
        username=new_user.username,
        firstName=new_user.firstName,
        lastName=new_user.lastName,
        telephoneNumber=new_user.telephoneNumber,
        yearsOfStudy=new_user_skills.yearOfStudy,
        fieldOfStudy=new_user_skills.fieldOfStudy,
        dateCreated=user.dateCreated
    )
    return user_out

@router.post("/new/employer", response_model=NewAccountCompanySchemaOut, status_code=status.HTTP_201_CREATED)
def new_employeer(user: NewAccountCompanySchemaIn, db: Session = Depends(get_db)):
    role = AccountRoles.employer

    user_exists = userRepository.get_user_by_username(user.username, db)
    unique_tel = userRepository.check_unique_telephone(user.telephoneNumber, db)
    if user_exists.first() != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists")
    if unique_tel.first() != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Telephone number: {user.telephoneNumber} already exists")

    user.password = utils.hash_pwd(user.password)
    new_user = models.UserAccount(
        username=user.username, 
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephoneNumber=user.telephoneNumber,
        dateCreated=user.dateCreated, 
        lastLogin=user.lastLogin
        )
    
    new_user = userRepository.create_new_user(new_user, db)

    account_role = models.AccountRoles(userAccountId = new_user.id, roles_id = role.value)
    account_role = userRepository.create_account_role(account_role, db)

    account_industry = user.industry.value
    industry_db_id = None

    for industry in IndustryDBMapper:
        if industry.name.lower() == account_industry.lower(): 
            industry_db_id = industry.value
            break

    company_details = models.CompanyDetails(
        companyName = user.companyName, 
        companyDescription = user.companyDescription,
        industry_id = industry_db_id
    )
    new_company = userRepository.create_new_company(company_details, db)
    
    user_company_link = models.CompanyRepresentative(
        company_id = new_company.id,
        userAccount_id = new_user.id
    )

    new_company_user_limnk = userRepository.create_user_company_link(user_company_link, db)

    # * update output values to include company , description, etc.
    user_out = NewAccountCompanySchemaOut(
        id=new_user.id,
        username=new_user.username,
        firstName=new_user.firstName,
        lastName=new_user.lastName,
        telephoneNumber=new_user.telephoneNumber,
        accountRoleId=role.value,
        company = new_company.companyName,
        dateCreated=user.dateCreated
    )
    return user_out

@router.post("/new/recruiter", status_code=status.HTTP_201_CREATED)
def new_recruiter(user: NewAccountCompanySchemaIn, db: Session = Depends(get_db)):

    role = AccountRoles.recruiter

    user_exists = userRepository.get_user_by_username(user.username, db)
    unique_tel = userRepository.check_unique_telephone(user.telephoneNumber, db)
    if user_exists.first() != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists")
    if unique_tel.first() != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Telephone number: {user.telephoneNumber} already exists")

    user.password = utils.hash_pwd(user.password)
    new_user = models.UserAccount(
        username=user.username, 
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephoneNumber=user.telephoneNumber,
        dateCreated=user.dateCreated, 
        lastLogin=user.lastLogin
        )
    
    new_user = userRepository.create_new_user(new_user, db)

    account_role = models.AccountRoles(userAccountId = new_user.id, roles_id = role.value)
    account_role = userRepository.create_account_role(account_role, db)

    account_industry = user.industry.value
    industry_db_id = None

    for industry in IndustryDBMapper:
        if industry.name.lower() == account_industry.lower(): 
            industry_db_id = industry.value
            break

    company_details = models.CompanyDetails(
        companyName = user.companyName, 
        companyDescription = user.companyDescription,
        industry_id = industry_db_id
    )
    new_company = userRepository.create_new_company(company_details, db)
    
    user_company_link = models.CompanyRepresentative(
        company_id = new_company.id,
        userAccount_id = new_user.id
    )

    new_company_user_limnk = userRepository.create_user_company_link(user_company_link, db)

    # * update output values to include company , description, etc.
    user_out = NewAccountCompanySchemaOut(
        id=new_user.id,
        username=new_user.username,
        firstName=new_user.firstName,
        lastName=new_user.lastName,
        telephoneNumber=new_user.telephoneNumber,
        accountRoleId=role.value,
        company = new_company.companyName,
        dateCreated=user.dateCreated
    )
    return user_out

#: --------- UPDATE ---------

@router.patch("/volunteer/update", response_model=UpdateVolunteerAccountSchema, status_code=status.HTTP_200_OK)
def account_update(user_update: UpdateVolunteerAccountSchema, db: Session = Depends(get_db)):

    user = userRepository.get_user_account_details_by_id(user_update.id, db)
    if user.all() == []: raise HTTPException(status.HTTP_409_CONFLICT, f"User with id: {user_update.id} does not exist | Try registering")

    existing_data = None

    for login, contact in user.all():
        existing_data = UpdateVolunteerAccountSchema(
            id=login.id,
            username=login.username,
            firstName=contact.firstName,
            lastName=contact.lastName,
            telephoneNumber=contact.telephoneNumber,
            experience="",
            fieldOfStudy="",
            degree="" 
        )
    update_data_dict = dict(user_update)
    existing_data_dict = dict(existing_data)

    #* compare existing user to new update and returns values changed
    changes = {value: update_data_dict[value] for value in update_data_dict if value in existing_data_dict and update_data_dict[value] != existing_data_dict[value]}    
    
    user_changes = {key:value for key, value in changes.items() if key == "username"}

 
    if user_changes: 
        user_id = existing_data_dict.get("id")
        updated_user = userRepository.update_user_account_by_id(user_id, user_changes, db)

    new_changes = UpdateAccountSchema(
        id=updated_user.id, 
        username=updated_user.username, 
        firstName=updated_contact_details.firstName,
        lastName=updated_contact_details.lastName, 
        telephoneNumber=updated_contact_details.telephoneNumber
    )
    return new_changes

@router.patch("/company/update", response_model=UpdateCompanyUserAccountSchema, status_code=status.HTTP_200_OK)
def account_update(user_update: UpdateCompanyUserAccountSchema, db: Session = Depends(get_db)):

    user = userRepository.get_user_account_details_by_id(user_update.id, db)
    if user.all() == []: raise HTTPException(status.HTTP_409_CONFLICT, f"User with id: {user_update.id} does not exist | Try registering")

    existing_data = None

    for login, contact in user.all():
        existing_data = UpdateCompanyUserAccountSchema(
            id=login.id,
            username=login.username,
            firstName=contact.firstName,
            lastName=contact.lastName,
            telephoneNumber=contact.telephoneNumber,
        )
    update_data_dict = dict(user_update)
    existing_data_dict = dict(existing_data)

    #* compare existing user to new update and returns values changed
    changes = {value: update_data_dict[value] for value in update_data_dict if value in existing_data_dict and update_data_dict[value] != existing_data_dict[value]}    
    
    user_changes = {key:value for key, value in changes.items() if key == "username"}

 
    if user_changes: 
        user_id = existing_data_dict.get("id")
        updated_user = userRepository.update_user_account_by_id(user_id, user_changes, db)

    new_changes = UpdateAccountSchema(
        id=updated_user.id, 
        username=updated_user.username, 
        firstName=updated_contact_details.firstName,
        lastName=updated_contact_details.lastName, 
        telephoneNumber=updated_contact_details.telephoneNumber
    )
    return new_changes


#: --------- READ ---------

@router.get("", status_code=status.HTTP_200_OK, response_model=List[schemas.UserOut])
def get_all_users(db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).all()

    if user_returned == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned

    
@router.get("/email", status_code=status.HTTP_200_OK)
def get_user_by_email(user: schemas.Email, db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.username == user.username).first()
    
    if not user_returned: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int,  db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.id == user_id).first()

    if user_returned == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user_job_history (user_id: int,  db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.id == user_id).first()

    if user_returned == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned



#: --------- DELETE ---------

@router.delete("/delete", status_code=status.HTTP_200_OK)
def delete_user_by_email(login: schemas.Email,  db: Session = Depends(get_db)): #,current_user: int = Depends(outh2.get_current_user)

    user_returned = userRepository.get_user_by_username(login.username, db)
    
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {login.username} does not exist")
    
    userRepository.delete_user_by_object(user_returned, db)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db),):

    user_returned = userRepository.get_user_by_id(user_id, db)
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")

    userRepository.delete_user_by_object(user_returned, db)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)