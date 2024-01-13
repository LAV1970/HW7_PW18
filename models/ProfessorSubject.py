from sqlalchemy import Column, Integer, String
from models import Base


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"
    professor_id = Column(
        Integer, ForeignKey("professor.professor_id"), primary_key=True
    )
    subject_id = Column(Integer, ForeignKey("subject.subject_id"), primary_key=True)

    professor = relationship("Professor", back_populates="subjects")
    subject = relationship("Subject", back_populates="professors")
