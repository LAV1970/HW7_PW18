from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Создаем движок для работы с базой данных SQLite
engine = create_engine(
    "sqlite:///F:\Projects\Python_projects\Alex\HW7_PW18", echo=True
)  # 'sqlite:///mydatabase.db' - путь к файлу базы данных SQLite

# Создаем базовый класс для объявления моделей
Base = declarative_base()


# Определяем модели для каждой таблицы
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()
