from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from Database.Connection import get_db
from Database.Tables import create_tables
from Routers import task_router, punishment_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(task_router.router)
app.include_router(punishment_router.router)


@app.get('/ChekConnection')
async def checkconnection(db: Session = Depends(get_db)):
    return {"message": "OK"}

#todo -> create get random punishment