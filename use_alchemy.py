from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

# Определение переменной Base перед использованием
Base = declarative_base()

DATABASE_URL = "sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db"
engine = create_engine(DATABASE_URL)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey("groupps.group_id"))
    group = relationship("Group", back_populates="students")


class Group(Base):
    __tablename__ = "groupps"
    group_id = Column(Integer, primary_key=True)
    name_group = Column(String(255))
    fach = Column(Integer)
    subject = Column(String(50))
    students = relationship("Student", back_populates="group")


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


metadata = MetaData()

professor_subject = Table(
    "professor_subject",
    metadata,
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
