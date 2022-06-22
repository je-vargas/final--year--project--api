from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, models, outh2, schemas
from ..Schemas.jobSchemas import *
from ..Services import enumDBMapper
from ..Services import enumMapper
from ..Repositories import jobRepository, userRepository


router = APIRouter(
    prefix="/jobs", 
    tags=["Jobs"]
)

#: --------------------------- CREATE ---------------------------
@router.post("/new", response_model=NewJobSchemaOut ,status_code=status.HTTP_200_OK)
def add_job(job: NewJobSchemaIn, current_user: schemas.TokenData = Depends(outh2.get_current_user), db: Session = Depends(database.get_db)):

    if current_user.role.lower() != 'employer':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    category_id = enumDBMapper.category_name_to_id_db_mapper(job.category.value)
    user = userRepository.get_company_account_details_by_id(current_user.id, db)

    companyLink = None

    for user, companyLink, companyDetails, industry, account, role in user.all():
        pass

    company_representative_id = companyLink.id

    new_job = models.Jobs(
        companyRepresentative_id = company_representative_id,
        category_id = category_id,
        description = job.description,
        title = job.title,
        numberOfPositions = job.numberOfPositions,
        onGoingFill = job.onGoingfill,
        startDate = job.startDate,
        endDate = job.endDate,
        applicationDeadline = job.applicationDeadLine,
        workHours = job.workHours.name,
    )

    new_job = jobRepository.create_new_job(new_job, db)
    category = enumDBMapper.category_id_to_name_db_mapper(new_job.category_id)
    hours = enumMapper.workHours_mapped_to_value(new_job.workHours)

    response = NewJobSchemaOut(
        category = category,
        description = new_job.jobDescription ,
        title = new_job.jobTitle,
        numberOfPositions = new_job.numberOfPositions,
        onGoingfill = new_job.onGoingFill,
        startDate = new_job.startDate,
        endDate = new_job.endDate,
        applicationDeadLine = new_job.applicationDeadline,
        workHours = hours,
    )

    return response

#: --------------------------- READ ---------------------------

@router.get("/search", response_model=JobCategoryEnum ,status_code=status.HTTP_200_OK)
def get_jobs_by_jobTitle(db: Session = Depends(database.get_db), limit: int = 0, skip: int = 0, search:Optional[str]=""):

    jobs_found = db.query(models.Jobs).filter(models.Jobs.jobTitle.coun).limit(limit).offset(skip).all()

    return jobs_found

#: --------------------------- UPDATE ---------------------------

@router.patch("/{job_id}/update", status_code=status.HTTP_200_OK)
def update_job(job_update: JobUpdateSchemaIn, job_id: int ,current_user: schemas.TokenData = Depends(outh2.get_current_user), db: Session = Depends(database.get_db)):

    if current_user.role.lower() != 'employer':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    employer_id = current_user.id
    job_user_match = jobRepository.get_job_by_id_and_employer_id(job_id, employer_id, db)

    for companyRep, job in job_user_match.all(): 
        if job == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"Job with id: {job_id} was not found") 

    job_category = enumDBMapper.category_id_to_name_db_mapper(job.category_id)
    job_hours = enumDBMapper.workHours_db_mapper(job.workHours)
    
    existing_job = JobUpdateSchemaIn(
        category = job_category,
        description = job.description,
        title = job.title,
        numberOfPositions = job.numberOfPositions,
        onGoingFill = job.onGoingFill,
        startDate = job.startDate,
        endDate = job.endDate,
        applicationDeadline = job.applicationDeadline,
        workHours = job_hours,
    )

    job_dict = dict(existing_job)
    job_update_dict = dict(job_update) 

    changes = {value: job_update_dict[value] for value in job_update_dict if value in job_dict and job_update_dict[value] != job_dict[value] and job_update_dict[value] != None }    
    
    job_changes = {key:value for key, value in changes.items()}

    if job_changes.get('category'): 
        job_category = job_changes.get('category').value
        job_changes['category_id'] = job_changes.pop('category')
        job_changes['category_id'] = enumDBMapper.category_name_to_id_db_mapper(job_category)

    updated_job = None
    if job_changes : updated_job = jobRepository.update_job_by_id(job_id, job_changes, db)
    else: updated_job = existing_job

    return updated_job


#: --------------------------- DELETE ---------------------------

@router.delete("/{job_id}/delete", status_code=status.HTTP_200_OK)
def delete_job(job_id: int, current_user: schemas.TokenData = Depends(outh2.get_current_user), db: Session = Depends(database.get_db)):

    if current_user.role.lower() != 'employer':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    employer_id = current_user.id
    job_user_match = jobRepository.get_job_by_id_and_employer_id(job_id, employer_id, db)

    for companyRep, job in job_user_match.all(): 
        if job == None: raise HTTPException(status.HTTP_404_NOT_FOUND, f"Job with id: {job_id} was not found") 

    job_object = jobRepository.get_job_by_id(job.id, db)
    jobRepository.delete_job_by_object(job_object, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


