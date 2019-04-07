from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class applicant(Base):
    __tablename__ = 'applicant'
    ID = Column(Integer, primary_key = True)
    Name = Column(String)
    Age = Column(Integer)
    Subject = Column(String)


