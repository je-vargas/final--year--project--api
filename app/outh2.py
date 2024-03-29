from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from . import schemas
from .config import settings
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRY_MINUTES = settings.access_token

oauth2_scheme =OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_tocken(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get("user_id")
        role:str = payload.get("role")

        if id and role is None: raise credentials_exception

        token_data = schemas.TokenData(id = id, role=role)
    except JWTError:  
        raise credentials_exception

    return token_data

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_access_tocken(token, credentials_exception)