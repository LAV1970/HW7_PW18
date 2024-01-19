from faker import Faker
import random
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from alembic import command
from alembic.config import Config

# Инициализация Alembic
alembic_cfg = Config(
    "F:\Projects\Python_projects\Alex\HW7_PW18\alembic"
)  # замените на фактический путь к вашему файлу alembic.ini
alembic_cfg.set_main_option("script_location", "alembic")

# Создание миграции
command.revision(alembic_cfg, autogenerate=True, message="Add group_id to students")
Base = declarative_base()
fake = Faker()


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    g_name = Column(String, nullable=False)


class ProfessorSubject(Base):
    __tablename__ = "professor_subject"

    professor_subject_id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey("professor.professor_id"))
    subject_id = Column(Integer, ForeignKey("groups.group_id"))


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    degree = Column(String)


class Student(Base):
    __tablename__ = "students"

    id_stud = Column(Integer, primary_key=True, autoincrement=True)
    name_stud = Column(String)
    group_id = Column(Integer, ForeignKey("groups.group_id"))


class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.id_stud"))
    subject_id = Column(Integer, ForeignKey("groups.group_id"))
    data = Column(Date)


# Создание движка и таблиц в базе данных
engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление групп
group_names = ["Group A", "Group B", "Group C"]
for name in group_names:
    group = Group(g_name=name)
    session.add(group)

# Добавление студентов
for _ in range(10):
    student = Student(name_stud=fake.name(), group_id=random.choice(group_names))
    session.add(student)

# Commit изменений в базу данных
session.commit()

# Закрытие сессии
session.close()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление профессоров
for _ in range(5):
    professor = Professor(
        name=fake.name(),
        degree=fake.random_element(elements=("Ph.D.", "M.Sc.", "D.Sc.")),
    )
    session.add(professor)

# Commit изменений в базу данных
session.commit()

# Добавление предметов
for name in [
    "Math",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "English",
    "Computer Science",
    "Art",
]:
    professor_subject = ProfessorSubject(
        professor_id=random.choice(session.query(Professor).all()),
        subject_id=random.choice(session.query(Group).all()),
    )
    session.add(professor_subject)

# Commit изменений в базу данных
session.commit()

# Закрытие сессии
session.close()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление оценок
for _ in range(10):
    grade = Grade(
        grade_name=fake.random_element(elements=(2, 3, 4, 5)),
        fach=fake.random_element(elements=(1, 2, 3, 4)),
        student_id=random.choice(session.query(Student).all()),
        subject_id=random.choice(session.query(Group).all()),
        data=fake.date_of_birth(),
    )
    session.add(grade)

# Commit изменений в базу данных
session.commit()

# Закрытие сессии
session.close()
