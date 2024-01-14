from sqlalchemy import Column, Integer, String, ForeignKey, Date  # Импорт типа Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    g_name = Column(String(255))  # Изменил имя атрибута

    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"

    id_stud = Column(Integer, primary_key=True, autoincrement=True)
    name_stud = Column(String)
    group_name = Column(String, ForeignKey("groups.g_name"))
    group = relationship("Group", back_populates="students")


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    degree = Column(String(50))


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"

    professor_id = Column(
        Integer, ForeignKey("professor.professor_id"), primary_key=True
    )
    subject_id = Column(
        Integer, ForeignKey("groups.g_name"), primary_key=True
    )  # Предполагается, что связь с группами

    professor = relationship("Professor")
    subject = relationship("Group")


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)  # Добавлено отсутствовавшее поле
    subject_id = Column(
        Integer, ForeignKey("groups.g_name")
    )  # Предполагается, что связь с группами

    subject = relationship("Group")


# Создание движка и таблиц в базе данных
engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)
