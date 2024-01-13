from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base  # Импортируйте Base напрямую из models.__init__


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    professors = relationship("Professor", secondary="professor_subject")
