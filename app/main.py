from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from . import models, config
from .database import engine
from .Routers import user, auth, health


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(user.router)
