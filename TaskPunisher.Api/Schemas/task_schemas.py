from pydantic import BaseModel, Field
from typing import Optional


class Task(BaseModel):
    """Task model"""

    id: int
    description: str
    isCompleted: bool

    model_config = {
        "from_attributes": True
    }


class TaskCreate(BaseModel):
    """Task create model"""

    description: str
    isCompleted: bool = Field(default=False)


class TaskUpdate(BaseModel):
    """Task update model"""

    description: Optional[str] = Field(default=None)
    isCompleted: Optional[bool] = Field(default=False)