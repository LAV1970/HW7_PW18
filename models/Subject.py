from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .models import Base  # Adjust the import path


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    professors = relationship("Professor", secondary="professor_subject")


Subject.__table_args__ = {"extend_existing": True}
