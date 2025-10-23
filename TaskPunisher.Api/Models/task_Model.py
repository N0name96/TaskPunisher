from sqlalchemy import String, Integer, Boolean, Column
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()



class Tasks(Base):
    '''Task model'''

    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    isCompleted = Column(Boolean, default=False)

