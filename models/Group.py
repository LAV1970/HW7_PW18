from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .models import Base  # Импортируйте Base напрямую из models.__init__


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, index=True)
    name_group = Column(String, index=True)
    fach = Column(Integer)
    subject = Column(String)

    students = relationship("Student", back_populates="group")
