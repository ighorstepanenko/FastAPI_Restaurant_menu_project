from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey

from database import Base


def get_uuid():
    return str(uuid4())[:10]


class Menus(Base):
    __tablename__ = "menus"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
    title = Column(String(50))
    description = Column(String(50))

    def response(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
        }


class Submenus(Base):
    __tablename__ = "submenus"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
    menu_id = Column(String, ForeignKey("menus.id", ondelete='CASCADE'))
    title = Column(String)
    description = Column(String)

    def response(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
        }


class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
    menu_id = Column(String, ForeignKey("menus.id", ondelete='CASCADE'))
    submenu_id = Column(String, ForeignKey("submenus.id", ondelete='CASCADE'))
    title = Column(String)
    description = Column(String)
    price = Column(String)

    def response(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": str(self.price)
        }
