from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name_group = Column(String, nullable=False)
    fach = Column(Integer, nullable=False)
    subject = Column(String, nullable=False)

    students = relationship("Student", back_populates="group")
