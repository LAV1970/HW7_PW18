from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=False)

    group = relationship("Group", back_populates="students")


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name_group = Column(String, nullable=False)
    fach = Column(Integer, nullable=False)
    subject = Column(String, nullable=False)

    students = relationship("Student", back_populates="group")


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    professors = relationship("Professor", secondary="professor_subject")


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    degree = Column(String(50))
    subjects = relationship("Subject", secondary="professor_subject")


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"
    professor_id = Column(
        Integer, ForeignKey("professor.professor_id"), primary_key=True
    )
    subject_id = Column(Integer, ForeignKey("subject.subject_id"), primary_key=True)

    professor = relationship("Professor", back_populates="subjects")
    subject = relationship("Subject", back_populates="professors")
