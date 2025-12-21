from pydantic import BaseModel, ConfigDict


class TaskBaseDTO(BaseModel):
    id: int
    title: str
    description: str
    isCompleted: bool

    model_config = ConfigDict(from_attributes=True)