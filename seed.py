from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random
from models import Student, Group, Professor, ProfessorSubject, Grade
from datetime import date

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

    # Создаем объект Student
    student = Student(name=name, age=age, group_id=group_id)

    # Добавляем студента в сессию
    session.add(student)


# Добавьте отношения после определения всех классов
Student.group = relationship("Group", back_populates="students")
Group.students = relationship("Student", back_populates="group")

# Добавление 40 случайных студентов в базу данных
for _ in range(40):
    add_random_student_to_db()

# Добавьте отношения после определения всех классов
Student.group = relationship("Group", back_populates="students")
Group.students = relationship("Student", back_populates="group")

# Сохраняем изменения в базе данных
session.commit()

# Закрываем сессию
session.close()
