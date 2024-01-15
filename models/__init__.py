from sqlalchemy.orm import relationship  # добавим импорт relationship
from .student7 import Student
from .group7 import Group
from .professor7 import Professor
from .professorsubject7 import ProfessorSubject
from .grade7 import Grade

# Add relationships after all classes are defined
Student.group = relationship("Group", back_populates="students")
Group.students = relationship("Student", back_populates="group")
