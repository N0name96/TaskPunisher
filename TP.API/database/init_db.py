from database.base import Base
from database.engine import async_engine

import Models


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)