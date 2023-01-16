from uuid import UUID
from pydantic import BaseModel
from typing import Optional


class Menus(BaseModel):
    id: UUID
    title: str
    description: str
    submenus_count: Optional[int]
    dishes_count: Optional[int]


class Submenus(BaseModel):
    id: UUID
    title: str
    description: str
    dishes_count: Optional[int]


class Dishes(BaseModel):
    id: UUID
    title: str
    description: str
    price: str
