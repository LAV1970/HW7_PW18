import sqlite3

# Подключение к базе данных (если она не существует, она будет создана)
connection = sqlite3.connect("F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")

# Создание объекта курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Создание таблицы student
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        age INTEGER,
        group_id INTEGER
    )
"""
)

# Создание таблицы groupps
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS groupps (
        group_id INTEGER PRIMARY KEY,
        name_group VARCHAR(255),
        fach INTEGER,
        subject VARCHAR(50)
    )
"""
)

# Создание таблицы professor
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS professor (
        professor_id INTEGER PRIMARY KEY,
        name VARCHAR(20),
        degree VARCHAR(50)
    )
"""
)

# Создание таблицы professor_subject
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS professor_subject (
        professor_id INTEGER,
        subject_id INTEGER
    )
"""
)

# Создание таблицы grade
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS grade (
        grade_id INTEGER PRIMARY KEY,
        grade_name INTEGER,
        fach INTEGER,
        student VARCHAR(20),
        data DATE,
        subject_id INTEGER
    )
"""
)

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
