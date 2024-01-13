import sys
from pathlib import Path

# Добавьте путь к каталогу вашего проекта
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Затем добавьте импорты классов из модуля models
from models import Student, Group, Professor, Subject, ProfessorSubject, Grade

from sqlalchemy.orm import Session
from faker import Faker
from sqlalchemy import create_engine
import random
from datetime import datetime, timedelta

fake = Faker()

# Подключение к базе данных
DATABASE_URL = "sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db"
engine = create_engine(DATABASE_URL)

# Создание сессии SQLAlchemy
session = Session(engine)

# Импорт Base из SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)


# Создание функций для генерации данных
def create_students(num_students, groups):
    students = []
    for _ in range(num_students):
        student = Student(
            name=fake.name(),
            age=random.randint(18, 25),
            group_id=random.choice(groups).group_id,
        )
        students.append(student)
    return students


def create_groups():
    groups_data = [
        {"name_group": "Group A", "fach": 1, "subject": "Math"},
        {"name_group": "Group B", "fach": 2, "subject": "Physics"},
        {"name_group": "Group C", "fach": 3, "subject": "Chemistry"},
    ]
    groups = [Group(**data) for data in groups_data]
    return groups


def create_professors(num_professors):
    professors = []
    for _ in range(num_professors):
        professor = Professor(
            name=fake.name(),
            degree=fake.random_element(elements=("PhD", "MSc", "MD")),
        )
        professors.append(professor)
    return professors


def create_subjects():
    subjects_data = [
        "Math",
        "Physics",
        "Chemistry",
        "History",
        "English",
        "Biology",
        "Computer Science",
        "Geography",
    ]
    subjects = [Subject(name=subject) for subject in subjects_data]
    return subjects


def create_professor_subjects(professors, subjects):
    professor_subjects = []
    for professor in professors:
        for _ in range(random.randint(1, 3)):  # Each professor teaches 1-3 subjects
            subject = random.choice(subjects)
            professor_subject = ProfessorSubject(
                professor_id=professor.professor_id, subject_id=subject.subject_id
            )
            professor_subjects.append(professor_subject)
    return professor_subjects


def create_grades(students, subjects):
    grades = []
    for student in students:
        for subject in subjects:
            grade = Grade(
                grade_name=random.randint(1, 5),
                fach=random.randint(1, 3),
                student=student.name,
                data=fake.date_between(start_date="-1y", end_date="today"),
                subject_id=subject.subject_id,
            )
            grades.append(grade)
    return grades


# Создание данных
groups = create_groups()
students = create_students(40, groups)
professors = create_professors(5)
subjects = create_subjects()

# Добавление данных в сессию и сохранение в базе данных
session.add_all(groups + students + professors + subjects)
session.commit()

# Добавление связей для ProfessorSubject
professor_subjects = create_professor_subjects(professors, subjects)
session.add_all(professor_subjects)
session.commit()

# Добавление данных об оценках
grades = create_grades(students, subjects)
session.add_all(grades)
session.commit()

# Закрытие сессии
session.close()
