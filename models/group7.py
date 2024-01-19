from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .professor7 import Professor  # Импорт класса Professor

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    g_name = Column(String, nullable=False)

    professors = relationship("Professor", back_populates="group")
    students = relationship("Student", back_populates="group")
