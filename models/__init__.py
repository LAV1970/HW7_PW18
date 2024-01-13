from .student import Student
from .group import Group
from .professor import Professor
from .professorsubject import ProfessorSubject
from .grade import Grade
from sqlalchemy.orm import relationship

# Add relationships after all classes are defined
Student.group = relationship("Group", back_populates="students")
Group.students = relationship("Student", back_populates="group")
