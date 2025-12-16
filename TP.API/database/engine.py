from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
BD_DIR = BASE_DIR / "BD"
BD_DIR.mkdir(parents=True, exist_ok=True)
BD_FILE = "TaskPunisher.db"


DATABASE_URL = f"sqlite+aiosqlite:///{BD_DIR}/TaskPunisher.db"


async_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)


AsyncSession = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session():
    async with AsyncSession() as session:
        yield session