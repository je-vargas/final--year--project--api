from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError, validator
from email_validator import validate_email, EmailNotValidError
from psycopg2.extras import RealDictCursor
import psycopg2
import time

class UserLogin(BaseModel):
    firstname: str
    lastname: str
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

    post = None

    try:
        valid_email = validate_email(new_user.username)
    except EmailNotValidError as error: 
        raise HTTPException(status.HTTP_400_BAD_REQUEST,f"{error}")

    # check user doens't exist otherwise add them
    cursor.execute(''' SELECT * FROM test WHERE username = %s ''', (new_user.username,))
    post = cursor.fetchone()

    if post != None: raise HTTPException(status.HTTP_409_CONFLICT, f"Email address: {new_user.username} already exists | Try resetting password")


    try: 
        # add user to system
        sql = "INSERT INTO test (firstname, lastname, username, password) VALUES (%s, %s, %s, %s) ON CONFLICT (username) DO NOTHING " 
        data = new_user.firstname, new_user.lastname, new_user.username, new_user.password
        cursor.execute(sql, (data,))
        connection.commit()

    except Exception as error: 
        print(f"\nError: {error}")

    return {"Successul": new_user}
    

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int):

    user_id = str(user_id)
    cursor.execute(''' SELECT * FROM test WHERE id = %s''', (user_id,))
    user = cursor.fetchone()

    if not user: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} was not found")

    return {"User": user}


@app.delete("/users/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_by_id(user_id: int):

    user_id = str(user_id)
    cursor.execute(''' DELETE FROM test WHERE id = (%s) RETURNING * ''', (user_id,))
    deleted_user = cursor.fetchone()
    connection.commit()

    if deleted_user == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"User with ID {user_id} does not exist")

    return Response(status.HTTP_204_NO_CONTENT)