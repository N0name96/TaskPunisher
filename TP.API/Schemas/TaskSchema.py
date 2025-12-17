from pydantic import BaseModel, Field
from typing import Optional


class TaskSchemaBase(BaseModel):
    id: int
    description: str
    isCompleted: bool

    model_config = {
        "from_attributes": True
    }


class CreateTaskSchema(BaseModel):
    description: str = Field(
        description="Descripcion de la tarea"
    )
    isCompleted: bool = Field(
        description="Condicional de si esta completa o no"
    )


class UpdateTaskSchema(BaseModel):
    description: Optional[str] = Field(
        description="Descripcion de la tarea"
    )
    isCompleted: Optional[bool] = Field(
        description="Condicional de si esta completa o no"
    )