from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    g_name = Column(String(255))  # Изменил имя атрибута

    students = relationship("Student", back_populates="group")
