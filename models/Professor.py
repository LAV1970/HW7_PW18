from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .models import Base  # Импортируйте Base напрямую из models.__init__


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    degree = Column(String(50))
    subjects = relationship("Subject", secondary="professor_subject")


Professor.__table_args__ = {"extend_existing": True}
