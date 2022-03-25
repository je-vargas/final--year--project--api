from typing import Optional
from enum import Enum
from datetime import datetime
from pydantic import (
    BaseModel, 
    validator, 
    EmailStr,
    )

class JobCategory(str, Enum):
    engineering='engineering'
    construction='constrution'
    healthSocialServices='health & social'
    education='education'
    legalOccupations='legal occupations'
    management ='management'
    ITOccupations='IT occupations'
    catering='caternig'
    other = 'other'

class NewJobSchemaIn(BaseModel):
    category: JobCategory
    jobDescription: str
    jobTitle: str
    numberOfPositions: int
    onGoingfill: bool
    startDate: Optional[datetime()]
    endDate: Optional[datetime()]
    applicationDeadLine: datetime()
    workingSchedule: Optional[str]



