from sqlalchemy import Column, Integer, String
from models import Base


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, index=True)
    name_group = Column(String, index=True)
    fach = Column(Integer)
    subject = Column(String)

    # Добавьте это отношение
    students = relationship("Student", back_populates="group")
