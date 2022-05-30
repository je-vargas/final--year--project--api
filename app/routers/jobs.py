from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, outh2, schemas
from ..Schemas.jobSchemas import NewJobSchemaIn, JobCategory


router = APIRouter(
    prefix="/jobs", 
    tags=["Jobs"]
)

@router.post("/new", response_model=NewJobSchemaIn ,status_code=status.HTTP_200_OK)
def add_job(new_job: NewJobSchemaIn, current_user: schemas.TokenData = Depends(outh2.get_current_user), db: Session = Depends(database.get_db)):

    if current_user.role != 'employer':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    print(new_job)
    # check the role of the user is employeer other wise they can't use this endpoint
    current_user.id

    
    

    #pull out data from dto and save to database

    return 


@router.get("/search", response_model=JobCategory ,status_code=status.HTTP_200_OK)
def get_jobs_by_jobTitle(db: Session = Depends(database.get_db), limit: int = 0, skip: int = 0, search:Optional[str]=""):

    jobs_found = db.query(models.Jobs).filter(models.Jobs.jobTitle.coun).limit(limit).offset(skip).all()

    return jobs_found



