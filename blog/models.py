from uuid import uuid4

from sqlalchemy import Column, Integer, String

from database import Base


def get_UUID():
    return str(uuid4())[:10]


class Menus(Base):
    __tablename__ = "menus"
    id = Column(String, primary_key=True, index=True, default=get_UUID)
    title = Column(String(50))
    description = Column(String(50))
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)


class Submenus(Base):
    __tablename__ = "submenus"
    id = Column(String, primary_key=True, index=True, default=get_UUID)
    title = Column(String)
    description = Column(String)
    dishes_count = Column(Integer, default=0)


class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(String, primary_key=True, index=True, default=get_UUID)
    title = Column(String)
    description = Column(String)
    price = Column(String)
