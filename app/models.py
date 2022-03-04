from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class ContactDetails(Base):
    __tablename__ = "contactDetails"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    emailAddress = Column(TIMESTAMP(timezone=True), unique=True, nullable=False)
    telephoneNumber = Column(TIMESTAMP(timezone=True), unique=True, nullable=False, server_default=text('now()'))

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    roles = Column(String, unique=True, nullable=False)

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, unique=True, nullable=False)

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
    contactDetails_id = Column(Integer, ForeignKey("contactDetails.id"), nullable=False)
    password = Column(String, nullable=False)
    dateCreated = Column(TIMESTAMP(timezone=True), nullable=False)
    lastLogin = Column(TIMESTAMP(timezone=True), nullable=False)
class VolunteerCV(Base):
    __tablename__ = "volunteerCV"

    id = Column(Integer, primary_key=True, index=True)
    userAccount_id = Column(Integer, ForeignKey("userAccount.id"), nullable=False)
    cv = Column(String, unique=True, nullable=True)

class VolunteerSkills(Base):
    __tablename__ = "volunteerSkills"

    id = Column(Integer, primary_key=True, index=True)
    userAccount_id = Column(Integer, ForeignKey("userAccount.id"), nullable=False)
    experience = Column(String)
    fieldOfStudy = Column(String)
    degree = Column(String)

class AccountRoles(Base):
    __tablename__ = "accountRoles"

    id = Column(Integer, primary_key=True, index=True)
    userAccountId = Column(Integer, ForeignKey("userAccount.id"), nullable=False)
    roles_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

class Employer(Base):
    __tablename__ = "employer"

    id = Column(Integer, primary_key=True, index=True)
    companyName = Column(Integer, ForeignKey("userAccount.id"), nullable=False)
    industry_id = Column(Integer, ForeignKey("industry.id"), nullable=False)
    companyDescription = Column(String, nullable=True)

class EmployerContacts(Base):
    __tablename__ = "employerContacts"

    id = Column(Integer, primary_key=True, index=True)
    ContactDetails_id = Column(Integer, ForeignKey("contactDetails.id"), nullable=False)
    employer_id = Column(Integer, ForeignKey("employer.id"), nullable=False)

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    employer_id = Column(Integer, ForeignKey("employer.id"), index=True)
    category_id = Column(Integer, ForeignKey("category.id"), index=True)
    jobDescription = Column(String, nullable=False)
    jobTitle = Column(String, nullable=False)
    numberOfPositions = Column(Integer, nullable=False)
    onGoingFill = Column(Boolean, nullable=False)
    startDate = Column(TIMESTAMP(timezone=True), nullable=True)
    endDate = Column(TIMESTAMP(timezone=True), nullable=True)
    applicationDeadline = Column(TIMESTAMP(timezone=True), nullable=True)


class JobSchedule(Base):
    __tablename__ = "jobSchedule"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), index=True)
    workingSchedule_id = Column(Integer, ForeignKey("workingSchedule.id"), index=True)

class UserVolunteeringHistory(Base):
    __tablename__ = "userVolunteeringHistory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("userAccount.id"), index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), index=True)

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    createdOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))




    