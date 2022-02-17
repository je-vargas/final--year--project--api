from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from .database import Base

class ContactDetails(Base):
    __tablename__ = "contactDetails"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    emailAddress = Column(Time, unique=True, nullable=False)
    telephoneNumber = Column(Time, unique=True, nullable=False)

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    roles = Column(String, unique=true, nullable=False)

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, unique=true, nullable=False)

class WorkingSchedule(Base):
    __tablename__ = "workingSchedule"
    
    id = Column(Integer, primary_key=True, index=True)
    schedule = Column(String(), index=True)

class Industry(Base):
    __tablename__ = "industry"

    id = Column(Integer, primary_key=True, index=True)
    industry = Column(String, nullable=False)

class UserAccount(Base):
    __tablename__ = "userAccount"

    id = Column(Integer, primary_key=True, index=True)
    contactDetails_id = Column(Integer, ForeignKey(contactDetails.id), nullable=False)
    password = Column(String, nullable=False)
    dateCreated = Column(Time, nullable=False)
    lastLogin = Column(Time, nullable=False)
class VolunteerCV(Base):
    __tablename__ = "volunteerCV"

    id = Column(Integer, primary_key=True, index=True)
    userAccount_id = Column(Integer, ForeignKey(userAccount.id), nullable=False)
    cv = Column(String, unique=True, nullable=True)

class VolunteerSkills(Base):
    __tablename__ = "volunteerSkills"

    id = Column(Integer, primary_key=True, index=True)
    userAccount_id = Column(Integer, ForeignKey(userAccount.id), nullable=False)
    experience = Column(String)
    fieldOfStudy = Column(String)
    degree = Column(String)

class AccountRoles(Base):
    __tablename__ = "accountRoles"

    id = Column(Integer, primary_key=True, index=True)
    userAccountId = Column(Integer, ForeignKey(userAccount.id), nullable=False)
    roles_id = Column(Integer, ForeignKey(roles.id), nullable=False)

class Employer(Base):
    __tablename__ = "employer"

    id = Column(Integer, primary_key=True, index=True)
    companyName = Column(Integer, ForeignKey(userAccount.id), nullable=False)
    industry_id = Column(Integer, ForeignKey(industry.id), nullable=False)
    companyDescription = Column(String, nullable=True)

class EmployerContacts(Base):
    __tablename__ = "employerContacts"

    id = Column(Integer, primary_key=True, index=True)
    ContactDetails_id = Column(Integer, ForeignKey(contactDetails.id), nullable=False)
    employer_id = Column(Integer, ForeignKey(employer.id), nullable=False)

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    employeers_id = Column(Integer, ForeignKey(employeers.id), index=True)
    category_id = Column(Integer, ForeignKey(category.id), index=True)
    jobDescription = Column(String, nullable=False)
    jobTitle = Column(String, nullable=False)
    numberOfPositions = Column(Integer, nullable=False)
    onGoingFill = Column(Boolean, nullable=False)
    startDate = Column(Time, nullable=True)
    endDate = Column(Time, nullable=True)
    applicationDeadline = Column(Time, nullable=True)


class JobSchedule(Base):
    __tablename__ = "jobSchedule"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey(jobs.id), index=True)
    workingSchedule_id = Column(Integer, ForeignKey(workingSchedule.id), index=True)

class UserVolunteeringHistory(Base):
    __tablename__ = "userVolunteeringHistory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(userAccount.id), index=True)
    job_id = Column(Integer, ForeignKey(jobs.id), index=True)




    