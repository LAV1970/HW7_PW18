from sqlalchemy import Column, Integer, String, ForeignKey, Date
from .base import Base  # Изменили эту строку
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    g_name = Column(String(255))  # Изменил имя атрибута

    students = relationship("Student", back_populates="group")
