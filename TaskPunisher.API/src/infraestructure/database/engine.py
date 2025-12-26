import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


# Ruta de bbdd en el proyecto
DB_PATH = "task_punisher.db"
DATABASE_URL = f"sqlite+aiosqlite:///./{DB_PATH}"


# Creamos el motor asicrono
engine = create_async_engine(
    url=DATABASE_URL,
    connect_args={"check_same_thread": False}, # Esta configuracion es necesaria para fastapi
    echo=True # Poner en false en entorno de produccion
)


# Configuramos fabrica de sesion
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)