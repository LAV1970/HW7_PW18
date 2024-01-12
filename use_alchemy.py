from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

# Определение переменной Base перед использованием
Base = declarative_base()

DATABASE_URL = "sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db"
engine = create_engine(DATABASE_URL)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name_group = Column(String, nullable=False)
    fach = Column(Integer, nullable=False)
    subject = Column(String, nullable=False)

    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=False)

    group = relationship("Group", back_populates="students")


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


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"
    professor_id = Column(
        Integer, ForeignKey("professor.professor_id"), primary_key=True
    )
    subject_id = Column(Integer, ForeignKey("subject.subject_id"), primary_key=True)

    professor = relationship("Professor", back_populates="subjects")
    subject = relationship("Subject", back_populates="professors")


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))
