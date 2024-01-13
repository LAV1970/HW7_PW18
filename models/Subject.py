from sqlalchemy import Column, Integer, String
from models import Base


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    professors = relationship("Professor", secondary="professor_subject")
