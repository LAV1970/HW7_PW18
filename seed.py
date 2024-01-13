import sqlite3
from faker import Faker
import random

# Подключение к базе данных
connection = sqlite3.connect("F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
cursor = connection.cursor()

# Создание объекта Faker
fake = Faker()


# Функция для добавления случайного студента
def add_random_student():
    name = fake.name()
    age = random.randint(18, 25)
    group_id = random.randint(
        1, 10
    )  # Предполагается, что у вас есть 10 групп с group_id от 1 до 10

    cursor.execute(
        """
        INSERT INTO student (name, age, group_id)
        VALUES (?, ?, ?)
        """,
        (name, age, group_id),
    )


# Добавление 40 случайных студентов
for _ in range(40):
    add_random_student()

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
