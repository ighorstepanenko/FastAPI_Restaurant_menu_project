import uuid
from typing import Optional

from pydantic import BaseModel


def get_uuid():
    return str(uuid.uuid4())


class Menus(BaseModel):
    title: str
    description: str


class ShowMenu(BaseModel):
    title: str
    description: str

    class Config():
        orm = True


class Submenus(BaseModel):
    id: Optional[str] = uuid.uuid4()
    title: str
    description: str
    dishes_count: Optional[int]


class ShowSubmenu(BaseModel):
    title: str
    description: str

    class Config():
        orm = True


class Dishes(BaseModel):
    id: Optional[str] = uuid.uuid4()
    title: str
    description: str
    price: str


class ShowDish(BaseModel):
    title: str
    price: str

    class Config():
        orm = True
