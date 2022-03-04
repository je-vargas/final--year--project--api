from typing import Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, outh2


router = APIRouter(
    prefix="/jobs", 
    tags=["Jobs"]
)

@router.post("/new", response_model=schemas.JobIn ,status_code=status.HTTP_200_OK)
def add_job(new_job: schemas.JobIn, db: Session = Depends(database.get_db), current_user: models.UserAccount = Depends(outh2.get_current_user)):

    current_user.id
    
    new_job.employer_id = current_user.id
    # new_job.category_id = #* get the id of the category

    db.add(instance)
    db.commit()
    db.refresh()
    
    return 

@router.get("/search", response_model=schemas.JobOut ,status_code=status.HTTP_200_OK)
def get_jobs_by_jobTitle(db: Session = Depends(database.get_db), limit: int = 0, skip: int = 0, search:Optional[str]=""):

    jobs_found = db.query(models.Jobs).filter(models.Jobs.jobTitle.coun).limit(limit).offset(skip).all()

    return jobs_found

