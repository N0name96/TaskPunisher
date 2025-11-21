from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from Database.Connection import get_db
from Database.Tables import create_tables
from Routers import task_router, punishment_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(task_router.router)
app.include_router(punishment_router.router)


@app.get('/')
async def checkconnection(db: Session = Depends(get_db)):
    return {"message": "OK"}