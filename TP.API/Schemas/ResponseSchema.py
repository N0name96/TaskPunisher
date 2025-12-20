from pydantic import BaseModel
from typing import TypeVar, Generic, Optional


T = TypeVar("T")


class ResponseSchemaBase(BaseModel, Generic[T]):
    """Objeto de respuesta generica de la api"""

    status: int
    message: str
    response: Optional[T] = None