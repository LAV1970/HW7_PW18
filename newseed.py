import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Grade  # Импортируйте свои модели


def create_student(session, name, group_id):
    # Логика создания студента
    student = Student(name_stud=name, group_id=group_id)
    session.add(student)
    session.commit()


def read_students(session):
    # Логика чтения студентов
    students = session.query(Student).all()
    for student in students:
        print(
            f"ID: {student.id_stud}, Name: {student.name_stud}, Group ID: {student.group_id}"
        )


def update_student(session, student_id, new_name):
    # Логика обновления студента
    student = session.query(Student).get(student_id)
    if student:
        student.name_stud = new_name
        session.commit()
        print(f"Student with ID {student_id} updated successfully.")
    else:
        print(f"Student with ID {student_id} not found.")


def delete_student(session, student_id):
    # Логика удаления студента
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")


def main():
    parser = argparse.ArgumentParser(
        description="CLI program for CRUD operations with a database."
    )
    parser.add_argument(
        "--action",
        choices=["create", "read", "update", "delete"],
        help="CRUD operation",
    )
    parser.add_argument(
        "--model",
        "-m",
        choices=["student", "grade"],
        help="Model to perform the operation on",
    )

    args = parser.parse_args()

    engine = create_engine(
        "sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db"
    )  # Замените на свой путь к базе данных
    Session = sessionmaker(bind=engine)
    session = Session()

    if args.action == "create" and args.model == "student":
        create_student(session, "John Doe", 1)
    elif args.action == "read" and args.model == "student":
        read_students(session)
    elif args.action == "update" and args.model == "student":
        update_student(session, 1, "Jane Doe")
    elif args.action == "delete" and args.model == "student":
        delete_student(session, 1)
    else:
        print("Invalid action or model.")


if __name__ == "__main__":
    main()
