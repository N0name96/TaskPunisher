from sqlalchemy import inspect

from Models.task_Model import Base as BaseTaskModel, Tasks
from Models.punishment_model import Base as BasePunishmentModel, Punishments
from .Connection import engine


def create_tables():
    """Function that creates tables in db"""
    inspector = inspect(engine)
    created_tables = inspector.get_table_names()

    table_names = Tasks.__name__, Punishments.__name__

    for table_name in table_names:
        if table_name not in created_tables:
            if table_name == Tasks.__name__:
                BaseTaskModel.metadata.create_all(bind=engine)
            elif table_name == Punishments.__name__:
                BasePunishmentModel.metadata.create_all(bind=engine)
            print(f'Table {table_name} created')