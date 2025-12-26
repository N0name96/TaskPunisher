from pydantic import BaseModel, Field, ConfigDict


class TaskModel(BaseModel):
    """Modelo base de tasks"""

    id: int
    title: str
    description: str
    is_completed: bool = False

    model_config = ConfigDict(from_attributes=True)