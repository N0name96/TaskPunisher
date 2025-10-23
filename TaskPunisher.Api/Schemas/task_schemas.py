from pydantic import BaseModel


class Task(BaseModel):
    '''Task model'''

    id: int
    description: str
    isCompleted: bool


class TaskCreate(BaseModel):
    '''Task create model'''

    description: str
    isCompleted: bool


class TaskUpdate(BaseModel):
    '''Task update model'''

    description: str
    isCompleted: bool