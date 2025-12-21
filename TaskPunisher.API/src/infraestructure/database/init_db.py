from typing import AsyncGenerator
from src.infraestructure.database.engine import AsyncSessionLocal, engine
from src.infraestructure.database.base import Base


# Injeccion de dependencias para Fastapi
async def get_db():
    async with AsyncSessionLocal() as db_session:
        yield db_session


async def create_tables():
    """
    Funcion que crea las tablas de la bbdd con los modelos de sqlalchemy
    :return:
    """

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)