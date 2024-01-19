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


# Добавьте еще функции select_2, select_3 и так далее для других запросов

if __name__ == "__main__":
    result = select_1()
    print(result)
