from email_validator import validate_email, EmailNotValidError
from fastapi import Depends, FastAPI, HTTPException, status, Response
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from typing import Optional, List
from . import models
from . import schemas
from .database import SessionLocal, engine, get_db 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




# #* q here is a query string passed in the url http://localhost:8000/items/5?q=somequery
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/")
def read_root():
    return {"Health": "OK"}


@app.post("/users/login", status_code=status.HTTP_201_CREATED, response_model=schemas.UserLogin)
async def user_login(new_user: schemas.UserLogin, db: Session = Depends(get_db)):

    try:
        valid_email = validate_email(new_user.username)
    except EmailNotValidError as error: 
        raise HTTPException(status.HTTP_400_BAD_REQUEST,f"{error}")

    user_exists = db.query(models.Test).filter(models.Test.username == new_user.username).first()

    if user_exists != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {new_user.username} already exists | Try resetting password")

    add_user = models.Test(**new_user.dict())
    db.add(add_user)
    db.commit()
    db.refresh(add_user)

    return new_user


@app.get("/users/", status_code=status.HTTP_200_OK, response_model=List[schemas.UserLogin])
def get_all_users(db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).all()

    if user_returned == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned

    
@app.get("/users/email", status_code=status.HTTP_200_OK)
def get_user_by_email(user: schemas.Email, db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.username == user.username).first()
    
    if not user_returned: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int,  db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.id == user_id).first()

    if user_returned == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return user_returned



@app.delete("/users/delete", status_code=status.HTTP_200_OK)
def delete_user_by_email(login: schemas.Email,  db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.username == login.username)

    if user_returned == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")

    user_returned.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/users/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_by_id(user_id: int,  db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.id == user_id)

    user_returned.delete(synchronize_session=False)
    db.commit()
    
    if deleted_user == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

