from pydantic import BaseModel, Field
from typing import Optional


class TaskBase(BaseModel):
    """Task model"""

    id: int = Field(description="Task id")
    description: str = Field(default="", description="Task description")
    isCompleted: bool = Field(default=False, description="Task status")

    model_config = {
        "from_attributes": True
    }


class TaskCreate(BaseModel):
    """Task create model"""

    description: str = Field(default="", description="Task description")
    isCompleted: bool = Field(default=False, description="Task status")


class TaskUpdate(BaseModel):
    """Task update model"""

    description: Optional[str] = Field(default=None, description="Task description")
    isCompleted: Optional[bool] = Field(default=False, description="Task status")