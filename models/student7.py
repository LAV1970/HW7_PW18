from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id_stud = Column(Integer, primary_key=True, autoincrement=True)
    name_stud = Column(String)
    group_name = Column(String, ForeignKey("groups.g_name"))
    group = relationship("Group", back_populates="students")


# Добавьте следующие строки после определения всех классов
from .group7 import Group

Student.group = relationship("Group", back_populates="students")
Group.students = relationship("Student", back_populates="group")
