from pydantic import BaseModel, Field


class Task(BaseModel):
    '''Task model'''

    id: int
    description: str
    isCompleted: bool

    model_config = {
        "from_attributes": True
    }


class TaskCreate(BaseModel):
    '''Task create model'''

    description: str
    isCompleted: bool = Field(default=False)


class TaskUpdate(BaseModel):
    '''Task update model'''
# TODO Hacerlo opcional
    description: str
    isCompleted: bool = Field(default=False)