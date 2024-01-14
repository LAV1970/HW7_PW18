from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey("groupps.group_id"))

    group = relationship("Group", back_populates="students", uselist=False)
