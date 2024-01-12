from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Создание подключения к базе данных
engine = create_engine(
    "sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db", echo=True
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Определение моделей


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey("groupps.group_id"))


class Group(Base):
    __tablename__ = "groupps"

    group_id = Column(Integer, primary_key=True)
    name_group = Column(String(255))
    fach = Column(Integer)
    subject = Column(String(50))
    students = relationship("Student", backref="group")


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    degree = Column(String(50))
    subjects = relationship("Subject", secondary="professor_subject")


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    professors = relationship("Professor", secondary="professor_subject")


professor_subject = Table(
    "professor_subject",
    Base.metadata,
    Column("professor_id", Integer, ForeignKey("professor.professor_id")),
    Column("subject_id", Integer, ForeignKey("subject.subject_id")),
)


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))


# Создание таблиц в базе данных
Base.metadata.create_all(engine)
