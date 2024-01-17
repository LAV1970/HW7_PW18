from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database.base import Base


class Student(Base):
    __tablename__ = "students"

    id_stud = Column(Integer, primary_key=True, autoincrement=True)
    name_stud = Column(String)  # Изменено имя атрибута
    group_name = Column(String, ForeignKey("groups.g_name"))
    group_id = Column(Integer, ForeignKey("groups.group_id"))  # Added group_id
    group = relationship("Group", back_populates="students")
