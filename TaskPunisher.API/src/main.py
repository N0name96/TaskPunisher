from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.infraestructure.database.init_db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="TaskPunisher",
    description="Api generada para manejar las acciones de la aplicación taskpunisher",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

