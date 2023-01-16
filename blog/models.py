from sqlalchemy import Column, Integer, String
from database import Base


class Menus(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    submenus_count = Column(Integer)
    dishes_count = Column(Integer)