# my_select.py

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Group

engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    # Найти 5 студентов с наибольшим средним баллом по всем предметам
    result = (
        session.query(
            Student.name_stud,
            func.avg(Grade.grade_name).label("average_grade"),
        )
        .join(Grade, Student.id_stud == Grade.student_id)
        .group_by(Student.name_stud)
        .order_by(func.avg(Grade.grade_name).desc())
        .limit(5)
        .all()
    )
    return result


def select_2():
    # Найти студента с наивысшим средним баллом по соответствующему предмету
    result = (
        session.query(
            Group.g_name.label("group_name"),
            func.avg(Grade.grade_name).label("average_grade"),
            Student.name_stud,
        )
        .join(Student, Group.group_id == Student.group_id)
        .join(Grade, Student.id_stud == Grade.student_id)
        .group_by(Group.g_name, Student.name_stud)
        .order_by(func.avg(Grade.grade_name).desc())
        .distinct(Group.g_name)
        .all()
    )
    return result


def select_3(subject_name):
    # Найти средний бал в группах по определенному предмету
    result = (
        session.query(
            Group.g_name,
            func.avg(Grade.grade_name).label("average_grade"),
        )
        .join(Grade, Grade.subject_id == Group.group_id)
        .filter(Grade.subject == subject_name)
        .group_by(Group.g_name)
        .all()
    )
    return result


def select_4():
    # Найти средний бал на потоке (по всей таблице оценок)
    result = session.query(
        func.avg(Grade.grade_name).label("average_grade"),
    ).scalar()
    return result


# Добавьте еще функции select_5 и так далее для других запросов

if __name__ == "__main__":
    result = select_1()
    print(result)
    result = select_2()
    print(result)
    # Пример использования
    subject_name = "Math"  # Замените на нужный предмет
    result = select_3(subject_name)
    print(result)
    # Пример использования
    result = select_4()
    print(result)
