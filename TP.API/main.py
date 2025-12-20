import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

from database.init_db import init_db
from Routers import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="TaskPunisher",
    lifespan=lifespan
)


app.include_router(task_router)
