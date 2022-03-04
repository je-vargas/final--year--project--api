from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from .. import database, schemas, models, utils, outh2

router = APIRouter(
    prefix="/authenticate",
    tags=["Authentication"]
    )

@router.get("", response_model=schemas.Token, status_code=status.HTTP_200_OK)
def authenticate(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.Test).filter(models.Test.username == user_credentials.username).first()

    if user == None: raise HTTPException(status.HTTP_404_NOT_FOUND, "Invaid credentials")

    pwd_match = utils.verify_pwd(user_credentials.password, user.password)

    if not pwd_match: HTTPException(status.HTTP_404_NOT_FOUND, "Invaid credentials")

    access_token = outh2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}