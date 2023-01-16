from uuid import UUID
from pydantic import BaseModel


class Menus(BaseModel):
    id: UUID
    name: str
    description: str
    submenu_count: int
    difhes_count: int


class Submenus(BaseModel):
    id: UUID
    name: str
    description: str
    difhes_count: int


class Dishes(BaseModel):
    id: UUID
    name: str
    description: str
    price: int
