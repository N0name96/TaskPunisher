from pydantic import BaseModel, Field
from typing import Optional




class PunishmentBase(BaseModel):
    """PunishmentModel"""

    id: int
    description: str
    isCompleted: bool

    model_config = {
        "from_attributes": True
    }



class PunishmentCreate(BaseModel):
    """Punishment Create Model"""

    description: str
    isCompleted: bool = Field(default=False)



class PunishmentUpdate(BaseModel):
    """Punishment Update Model"""

    description: Optional[str] = Field(default=None)
    isCompleted: Optional[bool] = Field(default=False)