from pydantic import BaseModel, Field
from typing import Optional


class PunishmentSchemaBase(BaseModel):
    id: int
    description: str
    isCompleted: bool

    model_config = {
        "from_attributes": True
    }


class CreatePunishmentSchema(BaseModel):
    description: str = Field(
        description="Descripcion del castigo"
    )
    isCompleted: bool = Field(
        description="Condicional que indica si está completo"
    )


class UpdatePunishmentSchema(BaseModel):
    description: Optional[str] = Field(
        description="Descripcion del castigo"
    )
    isCompleted: Optional[bool] = Field(
        description="Condicional que indica si está completo"
    )