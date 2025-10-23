import uvicorn
from fastapi import FastAPI, Depends
from sentry_sdk.session import Session

from Database.Connection import get_db
from Database.Tables import create_tables

app = FastAPI()

create_tables()


@app.get('/')
async def root():
    return {"message": "Helo world"}


@app.get('/ChekConnection')
async def CheckConnection(db: Session = Depends(get_db)):
    return {"message": "OK"}

