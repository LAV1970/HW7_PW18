from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Group  # Подставьте правильный путь к вашим моделям

engine = create_engine("sqlite:///F:/Projects/Python_projects/Alex/HW7_PW18/uni_hw7.db")
Session = sessionmaker(bind=engine)
session = Session()

# Проверьте, что сессия создана успешно
if session:
    print("Session created successfully.")

# Ваш код добавления групп
# ...

# Commit изменений
session.commit()

# Закрытие сессии
session.close()
