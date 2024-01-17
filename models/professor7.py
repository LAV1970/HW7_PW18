from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # Add this line
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    degree = Column(String)

    subjects = relationship("ProfessorSubject", back_populates="professor")
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    group = relationship("Group", back_populates="professors")
