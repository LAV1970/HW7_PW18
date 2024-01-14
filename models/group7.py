from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Group(Base):
    __tablename__ = "groupps"

    group_id = Column(Integer, primary_key=True)
    name_group = Column(String(255))
    fach = Column(Integer)
    subject = Column(String(50))

    students = relationship("Student", back_populates="group")
