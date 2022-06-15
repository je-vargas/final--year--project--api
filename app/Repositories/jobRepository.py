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