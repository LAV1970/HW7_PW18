from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    degree = Column(String(50))

    subjects = relationship("ProfessorSubject", back_populates="professor")
