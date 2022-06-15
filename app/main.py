from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .Routers import users, auth, health, jobs

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(jobs.router)
