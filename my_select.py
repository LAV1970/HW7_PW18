import sqlite3

# Подключение к базе данных
connection = sqlite3.connect("F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
cursor = connection.cursor()

# Выполнение SQL-запроса для просмотра данных в таблице student
cursor.execute("SELECT * FROM student")

# Получение результатов запроса
rows = cursor.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Закрытие соединения
connection.close()
