from typing import Optional, TypeVar, Generic
from pydantic import Field, BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    """Response generic model"""

    status_code: int = Field(default=200, description="Response code")
    message: str = Field(default="", description="Response message")
    response: Optional[T] = Field(default=None, description="Response data")

    model_config = {
        "from_attributes": True
    }