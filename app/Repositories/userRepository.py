from fastapi import Depends, HTTPException, status
from ..models import UserAccount, AccountRoles, Roles

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

def update_user_account_by_id(id, user, db):
    try:
        query = db.query(UserAccount).filter(UserAccount.id == id)
        query.update(user, synchronize_session=False)
        db.commit()
        user_update = query.first()
        
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)

    return user_update


def get_user_by_username(username, db):

    user = None
    try:
        user = db.query(UserAccount).filter(UserAccount.username == username)
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with username: {0} | Error: {1}\n".format(username, contact_details, e.orig.pgerror))
    
    return user

def get_user_by_id(user_id, db):

    user = None
    try:
        user = db.query(UserAccount).filter(UserAccount.id == user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with id: {0} | Error: {1}\n".format(user_id, e.orig.pgerror))
    
    return user

def check_unique_telephone(new_telephone, db):

    user = None
    try:
        user = db.query(UserAccount).filter(UserAccount.telephoneNumber == new_telephone)
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with telephone: {0} | Error: {1}\n".format(new_telephone, e.orig.pgerror))
    
    return user

def get_user_account_details_by_id(user_id, db):

    user_details = None
    try:
        user_details = db.query(UserAccount, AccountRoles, Roles).\
            filter(UserAccount.id == user_id).\
            join(AccountRoles).filter(AccountRoles.userAccountId == UserAccount.id).\
            join(Roles).filter(Roles.id == AccountRoles.roles_id)


    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with id: {0} | Error: {1}\n".format(user_id, e.orig.pgerror))
    
    return user_details

def get_user_account_details_by_username(username, db):

    user_details = None
    try:
        user_details = db.query(UserAccount, AccountRoles, Roles).\
            filter(UserAccount.username == username).\
            join(AccountRoles).filter(AccountRoles.userAccountId == UserAccount.id).\
            join(Roles).filter(Roles.id == AccountRoles.roles_id)

    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with id: {0} | Error: {1}\n".format(user_id, e.orig.pgerror))
    
    return user_details

def delete_user_by_object(user, user_contact, db):
    try:
        user.delete(synchronize_session=False)
        user_contact.delete(synchronize_session=False)
        db.commit()
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)
