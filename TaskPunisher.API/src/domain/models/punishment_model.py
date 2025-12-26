from pydantic import BaseModel, ConfigDict


class PunishmentModel(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool = False

    model_config = ConfigDict(from_attributes=True)