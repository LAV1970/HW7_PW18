from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database.base import Base


class Student(Base):
    __tablename__ = "students"

    id_stud = Column(Integer, primary_key=True, autoincrement=True)
    name_stud = Column(String)
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    group = relationship("Group", back_populates="students")
