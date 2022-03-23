from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from ..import models, utils, schemas, outh2
from ..Schemas.usersSchemas import NewAccountSchemaIn, NewAccountSchemaOut
from ..Repositories import userRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
    )

from enum import Enum

class AccountRoles(Enum):
    """Docstring for MyEnum."""
    volunteer = 1
    employer = 2
    recruiter = 3

@router.post("/new/volunteer", response_model=NewAccountSchemaOut, status_code=status.HTTP_201_CREATED)
def new_volunteer(user: NewAccountSchemaIn, db: Session = Depends(get_db)):

    role = AccountRoles.volunteer

    user_exists = userRepository.get_user_by_username(user.username, db)
    if user_exists != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists | Try resetting password")

    contact_details = models.ContactDetails(
        firstName=user.firstName,
        lastName=user.lastName,
        telephoneNumber=user.telephoneNumber
        )

    contact_details = userRepository.create_new_contact_details(contact_details, db)
    
    user.password = utils.hash_pwd(user.password)
    new_user = models.UserAccount(
        username=user.username, 
        password=user.password,
        contactDetails_id=contact_details.id, 
        dateCreated=user.dateCreated, 
        lastLogin=user.lastLogin
        )
    
    new_user = userRepository.create_new_user(new_user, db)

    account_role = models.AccountRoles(userAccountId = new_user.id, roles_id = role.value)

    account_role = userRepository.create_account_role(account_role, db)

    user_out = NewAccountSchemaOut(
        id=new_user.id,
        username=new_user.username,
        firstName=contact_details.firstName,
        lastName=contact_details.lastName,
        telephoneNumber=contact_details.telephoneNumber,
        accountRoleId=role.value,
        dateCreated=user.dateCreated
    )
    return user_out

@router.post("/new/employer", status_code=status.HTTP_201_CREATED)
def new_employeer(user: NewAccountSchemaIn, db: Session = Depends(get_db)):

    role = AccountRoles.employer

    user_exists = userRepository.get_user_by_username(user.username, db)
    if user_exists != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists | Try resetting password")

    contact_details = models.ContactDetails(
        firstName=user.firstName,
        lastName=user.lastName,
        telephoneNumber=user.telephoneNumber
        )

    contact_details = userRepository.create_new_contact_details(contact_details, db)
    
    user.password = utils.hash_pwd(user.password)
    new_user = models.UserAccount(
        username=user.username, 
        password=user.password,
        contactDetails_id=contact_details.id, 
        dateCreated=user.dateCreated, 
        lastLogin=user.lastLogin
        )
    
    new_user = userRepository.create_new_user(new_user, db)

    account_role = models.AccountRoles(userAccountId = new_user.id, roles_id = role.value)

    account_role = userRepository.create_account_role(account_role, db)

    user_out = NewAccountSchemaOut(
        id=new_user.id,
        username=new_user.username,
        firstName=contact_details.firstName,
        lastName=contact_details.lastName,
        telephoneNumber=contact_details.telephoneNumber,
        accountRoleId=role.value,
        dateCreated=user.dateCreated
    )
    return user_out

@router.post("/new/recruiter", status_code=status.HTTP_201_CREATED)
def new_recruiter(user: NewAccountSchemaIn, db: Session = Depends(get_db)):

    role = AccountRoles.recruiter

    user_exists = userRepository.get_user_by_username(user.username, db)
    if user_exists != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists | Try resetting password")

    contact_details = models.ContactDetails(
        firstName=user.firstName,
        lastName=user.lastName,
        telephoneNumber=user.telephoneNumber
        )

    contact_details = userRepository.create_new_contact_details(contact_details, db)
    
    user.password = utils.hash_pwd(user.password)
    new_user = models.UserAccount(
        username=user.username, 
        password=user.password,
        contactDetails_id=contact_details.id, 
        dateCreated=user.dateCreated, 
        lastLogin=user.lastLogin
        )
    
    new_user = userRepository.create_new_user(new_user, db)

    account_role = models.AccountRoles(userAccountId = new_user.id, roles_id = role.value)

    account_role = userRepository.create_account_role(account_role, db)

    user_out = NewAccountSchemaOut(
        id=new_user.id,
        username=new_user.username,
        firstName=contact_details.firstName,
        lastName=contact_details.lastName,
        telephoneNumber=contact_details.telephoneNumber,
        accountRoleId=role.value,
        dateCreated=user.dateCreated
    )
    return user_out










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



@router.delete("/delete", status_code=status.HTTP_200_OK)
def delete_user_by_email(login: schemas.Email,  db: Session = Depends(get_db), current_user: int = Depends(outh2.get_current_user)):

    user_returned = db.query(models.Test).filter(models.Test.username == login.username)
    
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {login.username} does not exist")
    
    user_returned.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db),):

    #: extend so it also deletes contact details

    user_returned = db.query(models.UserAccount).filter(models.UserAccount.id == user_id)
    
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")
    user_returned.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)