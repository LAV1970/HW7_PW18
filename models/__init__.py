from sqlalchemy.ext.declarative import declarative_base

# Создание declarative_base
Base = declarative_base()

# Создание сессии
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())


# Импорт всех модулей с помощью config.scan()
def includeme(config):
    config.scan(".models")


# from .student7 import Student
# from .group7 import Group
# from .professor7 import Professor
# from .professorsubject7 import ProfessorSubject
# from .grade7 import Grade
# from sqlalchemy.orm import relationship

# Add relationships after all classes are defined
# Student.group = relationship("Group", back_populates="students")
# Group.students = relationship("Student", back_populates="group")
