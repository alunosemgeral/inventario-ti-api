"""Equipment request and response schemas."""
from pydantic import BaseModel, Field

class EquipmentCreate(BaseModel):
    name: str = Field(min_length=1)
    category: str = Field(min_length=1)
    status: str = "available"

class EquipmentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    category: str | None = Field(default=None, min_length=1)
    status: str | None = None

class Equipment(EquipmentCreate):
    id: int