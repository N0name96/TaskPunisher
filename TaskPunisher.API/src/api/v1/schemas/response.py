from typing import Generic, TypeVar, Optional
from pydantic.v1.generics import GenericModel

T = TypeVar("T")

class StandardResponse(GenericModel, Generic[T]):
    status: int
    message: Optional[str] = None
    data: Optional[T] = None