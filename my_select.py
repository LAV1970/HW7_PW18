# my_select.py

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Group, Professor, ProfessorSubject

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


def select_5(professor_name):
    # Найти какие курсы читает соответствующий преподаватель
    result = (
        session.query(
            Group.g_name.label("group_name"),
            Professor.name.label("professor_name"),
        )
        .join(ProfessorSubject, Group.group_id == ProfessorSubject.subject_id)
        .join(Professor, ProfessorSubject.professor_id == Professor.professor_id)
        .filter(Professor.name == professor_name)
        .distinct(Group.g_name)
        .all()
    )
    return result


def select_6(group_name):
    # Найти список студентов в соответствующей группе
    result = (
        session.query(Student.name_stud)
        .join(Group, Student.group_id == Group.group_id)
        .filter(Group.g_name == group_name)
        .all()
    )
    return result


def select_7(group_name, subject_name):
    # Найти оценки студентов в отдельной группе по соответствующему предмету
    result = (
        session.query(
            Student.name_stud,
            Grade.grade_name,
        )
        .join(Group, Student.group_id == Group.group_id)
        .join(Grade, Student.id_stud == Grade.student_id)
        .filter(Group.g_name == group_name, Grade.subject == subject_name)
        .all()
    )
    return result


def select_8(professor_name):
    # Найти средний бал, который ставит соответствующий преподаватель по своему предмету
    result = (
        session.query(
            Professor.name.label("professor_name"),
            func.avg(Grade.grade_name).label("average_grade"),
        )
        .join(ProfessorSubject, Professor.professor_id == ProfessorSubject.professor_id)
        .join(Grade, ProfessorSubject.subject_id == Grade.subject_id)
        .filter(Professor.name == professor_name)
        .group_by(Professor.name)
        .all()
    )
    return result


def select_9(student_name):
    # Найти список курсов, которые посещает соответствующий студент
    result = (
        session.query(
            Group.g_name.label("group_name"),
            Grade.subject.label("subject_name"),
        )
        .join(Student, Group.group_id == Student.group_id)
        .join(Grade, Student.id_stud == Grade.student_id)
        .filter(Student.name_stud == student_name)
        .distinct(Group.g_name, Grade.subject)
        .all()
    )
    return result


def select_10(student_name, professor_name):
    # Список курсов, которые соответствующему студенту читает соответствующий преподаватель
    result = (
        session.query(
            Group.g_name.label("group_name"),
            Professor.name.label("professor_name"),
            Grade.subject.label("subject_name"),
        )
        .join(ProfessorSubject, Group.group_id == ProfessorSubject.subject_id)
        .join(Professor, ProfessorSubject.professor_id == Professor.professor_id)
        .join(Grade, ProfessorSubject.subject_id == Grade.subject_id)
        .join(Student, Group.group_id == Student.group_id)
        .filter(Student.name_stud == student_name, Professor.name == professor_name)
        .distinct(Group.g_name, Professor.name, Grade.subject)
        .all()
    )
    return result


if __name__ == "__main__":
    # Пример использования всех запросов
    result = select_1()
    print(result)
    result = select_2()
    print(result)
    subject_name = "Math"
    result = select_3(subject_name)
    print(result)
    result = select_4()
    print(result)
    professor_name = "Professor 1"
    result = select_5(professor_name)
    print(result)
    group_name = "Group 1"
    result = select_6(group_name)
    print(result)
    subject_name = "Math"
    result = select_7(group_name, subject_name)
    print(result)
    result = select_8(professor_name)
    print(result)
    student_name = "Student 1"
    result = select_9(student_name)
    print(result)
    result = select_10(student_name, professor_name)
    print(result)
