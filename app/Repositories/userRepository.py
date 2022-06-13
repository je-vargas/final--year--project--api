from fastapi import Depends, HTTPException, status
from ..models import UserAccount, AccountRoles, Roles, CompanyDetails, CompanyRepresentative, VolunteerSkills

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

def create_new_company(company: CompanyDetails, db):
    try:
        db.add(company)
        db.commit()
        db.refresh(company)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)

    return company

def create_user_company_link(company_rep: CompanyRepresentative, db):
    try:
        db.add(company_rep)
        db.commit()
        db.refresh(company_rep)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)

    return company_rep

def create_user_skills_link(user_skills: VolunteerSkills, db):
    try:
        db.add(user_skills)
        db.commit()
        db.refresh(user_skills)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)

    return user_skills

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

def get_user_account_company_details_by_id(user_id, db):

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
                select_from(UserAccount).\
                    filter(UserAccount.username == username).\
                join(AccountRoles).\
                    filter(AccountRoles.userAccountId == UserAccount.id).\
                join(Roles).\
                    filter(Roles.id == AccountRoles.roles_id)
        # print(user_details)

    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch user with username: {0} | Error: {1}\n".format(username, e.orig.pgerror))
    
    return user_details

def delete_user_by_object(user, db):
    try:
        user.delete(synchronize_session=False)
        db.commit()
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)
