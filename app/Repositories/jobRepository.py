from fastapi import HTTPException, status
from ..models import *

def create_new_job(new_job: Jobs, db):
    try:
        db.add(new_job)
        db.commit() 
        db.refresh(new_job)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, new_job, e.orig.pgerror)
        
    return new_job

def get_job_by_job_and_employer_id(job_id: int, employer_id: int, db):
    job = None
    try:
        job = db.query(CompanyRepresentative, Jobs).\
            join(Jobs, CompanyRepresentative.id == Jobs.companyRepresentative_id).\
            filter(CompanyRepresentative.userAccount_id == employer_id).\
            filter(Jobs.id == job_id)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch job for user with id: {0} | Error: {1}\n".format(employer_id, e.orig.pgerror))
    return job

def get_job_by_id(job_id: int, db):
    job = None
    try:
        job = db.query(Jobs).filter(Jobs.id == job_id)

    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "\nCouln't fetch job for user with id: {0} | Error: {1}\n".format(employer_id, e.orig.pgerror))
    return job


def delete_job_by_object(job_object, db):
    try:
        job_object.delete(synchronize_session=False)
        db.commit()
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)