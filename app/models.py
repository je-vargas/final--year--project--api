from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base

class ContactDetails(Base):
    __tablename__ = "contactDetails"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    telephoneNumber = Column(String, nullable=False, unique=True)

    def __repr__(self): 
        return "(%i, %s, %s, %s)" % (self.id, self.firstName, self.lastName, self.telephoneNumber)

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    roles = Column(String, unique=True, nullable=False)

    def __repr__(self): 
        return "({0})".format(self.roles)
class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category = Column(String, unique=True, nullable=False)
    industry_id = Column(Integer, ForeignKey("industry.id", ondelete="CASCADE"), nullable=False)

class Industry(Base):
    __tablename__ = "industry"

    id = Column(Integer, primary_key=True, index=True)
    industry = Column(String, nullable=False)

class UserAccount(Base):
    __tablename__ = "userAccount"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    contactDetails_id = Column(Integer, ForeignKey("contactDetails.id", ondelete="CASCADE"), nullable=False)
    dateCreated = Column(TIMESTAMP(timezone=True), nullable=False)
    lastLogin = Column(TIMESTAMP(timezone=True), nullable=False)

    def __repr__(self): 
        return "({0}, {1}, {2}, {3})".format(self.username, self.contactDetails_id ,self.dateCreated, self.lastLogin)
class VolunteerCV(Base):
    __tablename__ = "volunteerCV"

    id = Column(Integer, primary_key=True, index=True)
    userAccount_id = Column(Integer, ForeignKey("userAccount.id", ondelete="CASCADE"), nullable=False)
    cv = Column(String, unique=True, nullable=True)

class VolunteerSkills(Base):
    __tablename__ = "volunteerSkills"

    id = Column(Integer, primary_key=True, index=True)
    userAccount_id = Column(Integer, ForeignKey("userAccount.id", ondelete="CASCADE"), nullable=False)
    experience = Column(String)
    fieldOfStudy = Column(String)
    degree = Column(String)

class AccountRoles(Base):
    __tablename__ = "accountRoles"

    id = Column(Integer, primary_key=True, index=True)
    userAccountId = Column(Integer, ForeignKey("userAccount.id", ondelete="CASCADE"), nullable=False)
    roles_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    
    def __repr__(self): 
        return "({0}, {1})".format(self.userAccountId, self.roles_id)

class Employer(Base):
    __tablename__ = "employer"

    id = Column(Integer, primary_key=True, index=True)
    companyName = Column(Integer, ForeignKey("userAccount.id", ondelete="CASCADE"), nullable=False)
    industry_id = Column(Integer, ForeignKey("industry.id", ondelete="CASCADE"), nullable=False)
    companyDescription = Column(String, nullable=True)

class EmployerContacts(Base):
    __tablename__ = "employerContacts"

    id = Column(Integer, primary_key=True, index=True)
    ContactDetails_id = Column(Integer, ForeignKey("contactDetails.id", ondelete="CASCADE"), nullable=False)
    employer_id = Column(Integer, ForeignKey("employer.id", ondelete="CASCADE"), nullable=False)

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    employer_id = Column(Integer, ForeignKey("employer.id", ondelete="CASCADE"), index=True)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"), index=True)
    jobDescription = Column(String, nullable=False)
    jobTitle = Column(String, nullable=False)
    numberOfPositions = Column(Integer, nullable=False)
    onGoingFill = Column(Boolean, nullable=False)
    startDate = Column(TIMESTAMP(timezone=True), nullable=True)
    endDate = Column(TIMESTAMP(timezone=True), nullable=True)
    applicationDeadline = Column(TIMESTAMP(timezone=True), nullable=True)
    workHours = Column(String, nullable=True)

    employer = relationship("Employer")

class UserVolunteeringHistory(Base):
    __tablename__ = "userVolunteeringHistory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("userAccount.id", ondelete="CASCADE"), index=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), index=True)

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    createdOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    