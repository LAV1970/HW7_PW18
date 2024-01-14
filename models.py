from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Group(Base):
    __tablename__ = "groupps"

    group_id = Column(Integer, primary_key=True)
    name_group = Column(String(255))
    fach = Column(Integer)
    subject = Column(String(50))

    students = relationship("Student", back_populates="group", uselist=True)


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey("groupps.group_id"))

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
    subject_id = Column(Integer, ForeignKey("groupps.group_id"), primary_key=True)

    professor = relationship("Professor")
    subject = relationship("Group")


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String(20))
    data = Column(Date)
    subject_id = Column(Integer, ForeignKey("groupps.group_id"))

    subject = relationship("Group")


engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)
