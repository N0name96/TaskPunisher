from pydantic import BaseModel


class TaskCreateDTO(BaseModel):
    title: str
    description: str
    isCompleted: bool = False