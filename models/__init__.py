# Импорт всех модулей с помощью config.scan()
def includeme(config):
    config.scan(".models")


# Теперь перенесем импорты моделей вниз, после определения Base
from .base import Base
from .group7 import Group
from .student7 import Student
from .professor7 import Professor
from .professorsubject7 import ProfessorSubject
from .grade7 import Grade
from sqlalchemy.orm import relationship
