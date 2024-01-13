from sqlalchemy import Column, Integer, String
from models import Base


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    degree = Column(String(50))
    subjects = relationship("Subject", secondary="professor_subject")
