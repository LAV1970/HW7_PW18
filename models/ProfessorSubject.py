from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class ProfessorSubject(Base):
    __tablename__ = "professor_subjects"

    professor_subject_id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey("professors.professor_id"))
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"))

    professor = relationship("Professor", back_populates="professor_subjects")
    subject = relationship("Subject", back_populates="professor_subjects")
