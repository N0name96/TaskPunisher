from sqlalchemy import String, Integer, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Punishments(Base):
    __tablename__ = 'PunishmentS'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    isCompleted = Column(Boolean, default=False)
