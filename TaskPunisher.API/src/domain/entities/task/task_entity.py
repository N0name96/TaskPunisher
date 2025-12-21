from sqlalchemy import Column, Integer, String, Boolean

from src.infraestructure.database.base import Base


class Tasks(Base):
    __tablename__ = 'tasks'

    id =  Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    isCompleted = Column(Boolean, nullable=False, default=False)