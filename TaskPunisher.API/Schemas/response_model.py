from typing import Optional, Any
from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    """Response model"""

    status_code: int = Field(default=200, description="Response code")
    message: str = Field(default="", description="Response message")
    response: Optional[Any] = Field(default=None, description="Response data")