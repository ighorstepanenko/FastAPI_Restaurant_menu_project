from sqlalchemy import Column, Integer, String

from database import Base


class Menus(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    submenus_count = Column(Integer)
    dishes_count = Column(Integer)


class Submenus(Base):
    __tablename__ = "submenus"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    dishes_count = Column(Integer)


class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(String)
