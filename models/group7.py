from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database.base import Base


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    g_name = Column(String, nullable=False)

    professors = relationship("Professor", back_populates="group")
    students = relationship(
        "Student", back_populates="group"
    )  # Added back_populates for students
