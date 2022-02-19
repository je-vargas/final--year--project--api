from email_validator import validate_email, EmailNotValidError
from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from typing import Optional, List
from . import models
from . import utils
from . import schemas
from .database import SessionLocal, engine, get_db 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def health_check():
    return {"Health": "OK"}


@app.get("/token")
def authorise(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# @app.post("/users/login", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
@app.post("/users/login", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):

    try:
        valid_email = validate_email(user.username)
    except EmailNotValidError as error: 
        raise HTTPException(status.HTTP_400_BAD_REQUEST,f"{error}")

    user_exists = db.query(models.Test).filter(models.Test.username == user.username).first()

    if user_exists != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {user.username} already exists | Try resetting password")

    user.password = utils.get_password_hash(user.password)
    new_user = models.Test(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    print(type(new_user))

    return {new_user}


@app.get("/users/", status_code=status.HTTP_200_OK, response_model=List[schemas.UserOut])
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
    
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {login.username} does not exist")
    
    user_returned.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/users/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_by_id(user_id: int,  db: Session = Depends(get_db)):

    user_returned = db.query(models.Test).filter(models.Test.id == user_id)
    
    if user_returned.first() == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")

    user_returned.delete(synchronize_session=False)
    db.commit()
    

    return Response(status_code=status.HTTP_204_NO_CONTENT)







# #* q here is a query string passed in the url http://localhost:8000/items/5?q=somequery
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
