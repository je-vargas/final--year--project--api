from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, utils, schemas, outh2

router = APIRouter(
    prefix="/users",
    tags=["Users"]
    )

@router.post("/new", status_code=status.HTTP_201_CREATED)
def new_account(user: schemas.UserIn, db: Session = Depends(get_db)):

    user_exists = db.query(models.Test).filter(models.Test.username == user.username).first()

    if user_exists != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists | Try resetting password")

    user.password = utils.hash_pwd(user.password)
    new_user = models.Test(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {new_user}


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
def delete_user_by_id(user_id: int = Depends(outh2.get_current_user),  db: Session = Depends(get_db),):

    user_returned = db.query(models.Test).filter(models.Test.id == user_id)
    
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")
    user_returned.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)