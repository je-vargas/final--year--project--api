from typing import Optional
from enum import Enum
from datetime import date
from pydantic import (
    BaseModel, 
    validator, 
    EmailStr,
    )


class JobSchedule(str, Enum):
    fullTime = 'Full Time',
    partTime = 'Part Time',
    flexible = 'Flexible',

class WorkHours(str, Enum):
    sixMore = '6+',
    fourMore = '4-6',
    twoMore = '2-4',
    zeroMore = '0-2',
class JobCategory(str, Enum):
    aircraftDispatcher = 'Aircraft Dispatcher',
    aircraftMechanic = 'Aircraft Mechanic',
    airlinePilot = 'Airline Pilot',
    airMarshall = 'Air Marshall',
    flightAttendant = 'Flight Attendant',
    trafficAir = 'Traffic Air',
    actor = 'Actor ',
    museumJobs = 'Museum Jobs',
    musicCondutor = 'Music Condutor',
    accountant  = 'Accountant ',
    administrativeAssistant = 'Administrative Assistant',
    advertising  = 'Advertising ',
    financial  = 'Financial ',
    operations  = 'Operations ',
    management  = 'Management ',
    consultancy  = 'Consultancy ',
    financialAdvisor = "Financial Advisor",
    goverment  = 'Goverment ',
    humanResources = 'Human Resources',
    insuranceAgent = 'Insurance Agent',
    investmentBanker = 'Investment Banker',
    lawyer  = 'Lawyer ',
    teaching  = 'Teaching ',
    policeOffice = 'Police Office',
    doctor  = 'Doctor ',
    forensicPsychologist = 'Forensic Psychologist',
    nurse  = 'Nurse ',
    midwife  = 'Midwife ',
    veterinarian  = 'Veterinarian ',
    psychologist  = 'Psychologist ',
    waiter = 'Waiter ',
    sales = 'Sales ',
    backendDeveloper = 'Backend Developer',
    systemsAdministrator = 'Systems Administrator',
    softwareEngineer = 'Software Engineer',
    developer  = 'Developer ',
    architect  = 'Architect ',
    other = 'Other'

class NewJobSchemaIn(BaseModel):
    jobCategory: JobCategory
    jobSchedule: JobSchedule
    workHours: WorkHours
    jobDescription: str
    jobTitle: str
    numberOfPositions: int
    onGoingfill: bool
    startDate: date
    endDate: Optional[date]
    applicationDeadLine: date
    workingSchedule: Optional[str]



