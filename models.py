from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.types import Date  # Add this import for the Date type

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    g_name = Column(String, nullable=False)

    professors = relationship("Professor", back_populates="group")
    students = relationship(
        "Student", back_populates="group"
    )  # Added back_populates for students


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    degree = Column(String)

    subjects = relationship("ProfessorSubject", back_populates="professor")
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    group = relationship("Group", back_populates="professors")


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"

    professor_id = Column(
        Integer, ForeignKey("professor.professor_id"), primary_key=True
    )
    subject_id = Column(Integer, ForeignKey("groups.group_id"), primary_key=True)

    professor = relationship("Professor", back_populates="subjects")
    subject = relationship("Group", back_populates="professors")


class Student(Base):
    __tablename__ = "students"

    id_stud = Column(Integer, primary_key=True, autoincrement=True)
    name_stud = Column(String)  # Изменено имя атрибута
    group_name = Column(String, ForeignKey("groups.g_name"))
    group_id = Column(Integer, ForeignKey("groups.group_id"))  # Added group_id
    group = relationship("Group", back_populates="students")


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)  # Добавлено отсутствовавшее поле
    subject_id = Column(
        Integer, ForeignKey("groups.group_id")
    )  # Предполагается, что связь с группами

    subject = relationship("Group")


# Создание движка и таблиц в базе данных
engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)
