from sqlalchemy import Column, Integer, String
from models import Base


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))
