from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError, validator
from email_validator import validate_email, EmailNotValidError
from psycopg2.extras import RealDictCursor
import psycopg2
import time

class UserLogin(BaseModel):
    username: str
    password: str
    created: Optional[datetime] = None

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

#: -------------------------------------------- DB Connection -------------------------------------------- !

while True:
    try:
        connection = psycopg2.connect(
            host = 'localhost', 
            database = 'elvolunteer', 
            user = 'juanestebanvargassalamanca', 
            cursor_factory = RealDictCursor)
        cursor = connection.cursor()
        print("Fatty Database is wired up --- COFFEEEEE!!")
        break
    except Exception as err:
        print("\nConnection to Database - Junglesn Massive Failed")
        print(f"\nError: {err}")
        time.sleep(3)

#: -------------------------------------------- ENPOINTS -------------------------------------------- !
#: Order of endpoints matter!

app = FastAPI()

@app.get("/")
def read_root():
    return {"Health": "OK"}
# #* q here is a query string passed in the url http://localhost:8000/items/5?q=somequery
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/users/login", status_code=status.HTTP_201_CREATED)
async def user_login(new_user : UserLogin):
    try:
        valid_email = validate_email(new_user.username)
    except EmailNotValidError as error: 
        raise HTTPException(status.HTTP_400_BAD_REQUEST,f"{error}")

    try: 
        # check user doens't exist otherwise add them
        cursor.execute(f''' SELECT * FROM test WHERE id = {new_user.username} ''')
        post = cursor.fetchone()
    except Exception as error: 
        print(f"\nError: {error}")


    if post == None or post == '':
        try: 
        # add user to system
            cursor.execute(f''' SELECT * FROM test WHERE id = {new_user.username} ''')
            post = cursor.fetchone()
        except Exception as error: 
            print(f"\nError: {error}")





    return {"Successul": new_user}
    