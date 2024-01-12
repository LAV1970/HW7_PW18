from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


metadata = MetaData()

professor_subject = Table(
    "professor_subject",
    metadata,
    Column("professor_id", Integer, ForeignKey("professor.professor_id")),
    Column("subject_id", Integer, ForeignKey("subject.subject_id")),
)
