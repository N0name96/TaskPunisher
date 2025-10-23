from sqlalchemy import inspect

from Models.task_Model import Base, Tasks
from .Connection import engine


def create_tables():
    '''Function that creates tables in db'''
    inspector = inspect(engine)

    table_name = Tasks.__name__

    if table_name not in inspector.get_table_names():
        print('Tables will be create')
        Base.metadata.create_all(bind=engine)
        print('Tables ')
