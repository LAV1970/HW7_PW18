from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .models import Base


class Grade(Base):
    __tablename__ = "grades"

    grade_id = Column(Integer, primary_key=True, index=True)
    grade_name = Column(Integer)
    fach = Column(Integer)
    student = Column(String)
    data = Column(Date)  # Используйте Date из модуля datetime
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"))

    subject = relationship("Subject", back_populates="grades")


Grade.__table_args__ = {"extend_existing": True}
