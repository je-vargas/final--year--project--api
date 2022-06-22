from typing import Optional
from datetime import date
from ..globalEnums import WorkHoursEnum, JobCategoryEnum
from pydantic import (
    BaseModel, 
    validator, 
    EmailStr,
    )

class NewJobSchemaIn(BaseModel):
    category: JobCategoryEnum
    description: str
    title: str
    numberOfPositions: int
    onGoingFill: bool
    startDate: Optional[date]
    endDate: Optional[date]
    applicationDeadline: Optional[date]
    workHours: Optional[WorkHoursEnum]

class NewJobSchemaOut(BaseModel):
    category: JobCategoryEnum
    description: str
    title: str
    numberOfPositions: int
    onGoingFill: bool
    startDate: Optional[date]
    endDate: Optional[date]
    applicationDeadline: Optional[date]
    workHours: Optional[WorkHoursEnum]

class JobUpdateSchemaIn(BaseModel):
    category: Optional[JobCategoryEnum] = None
    description: Optional[str] = None
    title: Optional[str] = None
    numberOfPositions:Optional[int]
    onGoingFill:Optional[bool]
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    applicationDeadline: Optional[date] = None
    workHours: Optional[WorkHoursEnum] = None


