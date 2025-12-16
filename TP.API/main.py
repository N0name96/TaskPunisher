import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pygments.styles.dracula import yellow

from database.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="TaskPunisher",
    lifespan=lifespan
)
