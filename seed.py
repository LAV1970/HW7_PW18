from models.group7 import Group
from models.student7 import Student
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Создание объекта Faker
fake = Faker()


# Функция для добавления случайного студента с использованием SQLAlchemy
def add_random_student_to_db():
    name = fake.name()
    age = random.randint(18, 25)
    group_id = random.randint(1, 10)

    # Получаем случайную группу
    group = session.query(Group).filter_by(group_id=group_id).first()

    # Создаем объект Student
    student = Student(name=name, age=age, group=group)

    # Добавляем студента в сессию
    session.add(student)


# Добавление 40 случайных студентов в базу данных
for _ in range(40):
    add_random_student_to_db()

# Сохраняем изменения в базе данных
session.commit()

# Закрываем сессию
session.close()
