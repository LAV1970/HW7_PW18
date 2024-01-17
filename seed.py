from faker import Faker
import random
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from models import Group, Professor, ProfessorSubject, Grade, Student

Base = declarative_base()


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"

    professor_id = Column(
        Integer, ForeignKey("professor.professor_id"), primary_key=True
    )
    subject_id = Column(Integer, ForeignKey("groups.group_id"), primary_key=True)

    professor = relationship("Professor", back_populates="subjects")
    subject = relationship("Group", back_populates="professors")

    # Create a Faker object


fake = Faker()


# Создание движка и таблиц в базе данных
engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


# Создание групп
def add_group(name):
    group = Group(g_name=name)
    session.add(group)


group_names = ["Group A", "Group B", "Group C"]
for name in group_names:
    add_group(name)

# Commit изменений в базу данных
session.commit()


# Функция для добавления профессора в базу данных
def add_professor(name, degree):
    professor = Professor(name=name, degree=degree)
    session.add(professor)


# Добавление пяти профессоров
for _ in range(5):
    name = fake.name()
    degree = fake.random_element(elements=("Ph.D.", "M.Sc.", "D.Sc."))
    add_professor(name, degree)

# Commit изменений в базу данных
session.commit()

# Подгрузим профессоров в сессию перед созданием предметов
professors = session.query(Professor).all()

# Закрытие сессии
session.close()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление предметов
subject_names = [
    "Math",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "English",
    "Computer Science",
    "Art",
]

for name in subject_names:
    random_professor = random.choice(professors)
    random_group = random.choice(session.query(Group).all())

    subject = ProfessorSubject(
        name=name, professor=random_professor, group=random_group
    )

    session.add(subject)

# Commit изменений в базу данных
session.commit()

# Закрытие сессии
session.close()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление оценок
students = session.query(Student).all()
subjects = session.query(ProfessorSubject).all()

for student in students:
    for subject in subjects:
        value = fake.random_element(elements=(2, 3, 4, 5))
        grade = Grade(value=value, student=student.name_stud, subject=subject.name)
        session.add(grade)

# Commit изменений в базу данных
session.commit()

# Закрытие сессии
session.close()
