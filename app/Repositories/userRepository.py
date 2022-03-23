from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import ContactDetails, UserAccount, AccountRoles

def create_new_contact_details(contact_details: ContactDetails , db):
    try:
        db.add(contact_details)
        db.commit()
        db.refresh(contact_details)
    except Exception as e:
        # raise HTTPException(status.HTTP_400_BAD_REQUEST, "Unable to create new contact:{0} | Error: {1}\n".format(contact_details, contact_details, e.orig.pgerror))
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)
    
    return contact_details

def create_new_user(new_user: UserAccount, db):
    try:
        db.add(new_user)
        db.commit() 
        db.refresh(new_user)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, contact_details, e.orig.pgerror)
        
    return new_user

def create_account_role(account_role: AccountRoles, db):
    try:
        db.add(account_role)
        db.commit()
        db.refresh(account_role)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)

    return account_role

def get_user_by_username(username, db):

    user = None
    try:
        user = db.query(UserAccount).filter(UserAccount.username == username).first()
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with username: {0} | Error: {1}\n".format(username, contact_details, e.orig.pgerror))
    
    return user
