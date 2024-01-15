from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database.base import Base  # Импорт Base из правильного места


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    g_name = Column(String(255))

    students = relationship("Student", back_populates="group")


# Переместите этот импорт в самый конец файла
from .student7 import Student
