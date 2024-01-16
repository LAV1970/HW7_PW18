from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Group, Professor, ProfessorSubject, Grade, Student

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Создание движка и таблиц в базе данных
engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker object
fake = Faker()


# Function to add a group to the database
def add_group(name):
    group = Group(g_name=name)
    session.add(group)


# Add three groups
group_names = ["Group A", "Group B", "Group C"]
for name in group_names:
    add_group(name)

# Commit changes to the database
session.commit()


# Function to add a professor to the database
def add_professor(name, degree):
    professor = Professor(name=name, degree=degree)
    session.add(professor)


# Add five professors
for _ in range(5):
    name = fake.name()
    degree = fake.random_element(elements=("Ph.D.", "M.Sc.", "D.Sc."))
    add_professor(name, degree)

# Commit changes to the database
session.commit()

# Подгрузим профессоров в сессию перед созданием предметов
professors = session.query(Professor).all()

# Close the session
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

# Подгрузим профессоров и группы в сессию
professors = session.query(Professor).all()
groups = session.query(Group).all()

for name in subject_names:
    # Выберем случайного профессора и группу
    random_professor = fake.random_element(elements=professors)
    random_group = fake.random_element(elements=groups)

    subject = ProfessorSubject(
        name=name, professor=random_professor, group=random_group
    )
    session.add(subject)

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

session.commit()

# Закрытие сессии
session.close()
