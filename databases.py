from model import *

from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_applicant(Name , Age , Subject):
    applicant_obj = applicant(
        Name = Name,
        Age= Age,
        Subject = Subject)
    session.add(applicant_obj)
    session.commit()
    return applicant_obj
def query_all():
    applicants = session.query(applicant).all()
    return applicants