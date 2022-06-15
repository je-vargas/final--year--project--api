from typing import Optional
from datetime import date
from ..globalEnums import WorkHoursEnum, JobCategoryEnum
from pydantic import (
    BaseModel, 
    validator, 
    EmailStr,
    )

class NewJobSchemaIn(BaseModel):
    jobCategory: JobCategoryEnum
    jobDescription: str
    jobTitle: str
    numberOfPositions: int
    onGoingfill: bool
    startDate: Optional[date]
    endDate: Optional[date]
    applicationDeadLine: Optional[date]
    workHours: Optional[WorkHoursEnum]

class NewJobSchemaOut(BaseModel):
    jobCategory: JobCategoryEnum
    jobDescription: str
    jobTitle: str
    numberOfPositions: int
    onGoingfill: bool
    startDate: Optional[date]
    endDate: Optional[date]
    applicationDeadLine: Optional[date]
    workHours: Optional[WorkHoursEnum]



