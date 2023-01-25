import uuid
from typing import Optional

from pydantic import BaseModel


class Menus(BaseModel):
    title: str
    description: str



class Submenus(BaseModel):
    id: Optional[str] = uuid.uuid4()
    title: str
    description: str




class Dishes(BaseModel):
    id: Optional[str] = uuid.uuid4()
    title: str
    description: str
    price: str


