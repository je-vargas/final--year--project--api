from fastapi import FastAPI
from .Routers import users, auth, health, jobs

app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(jobs.router)
