from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey("groups.group_id"))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")
