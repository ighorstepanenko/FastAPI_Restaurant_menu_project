from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import Session, relationship

from database import Base


def get_uuid():
    return str(uuid4())[:10]


class Menus(Base):
    __tablename__ = "menus"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
    title = Column(String(50))
    description = Column(String(50))

    def response(self, db: Session):
        submenus = db.query(Submenus).filter(self.id == Submenus.menu_id)
        submenus_count = submenus.count()
        dishes_count = 0
        if not submenus_count:
            pass
        else:
            for i in submenus:
                dishes_count += i.response(db)["dishes_count"]
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "submenus_count": submenus_count,
            "dishes_count": dishes_count
        }


class Submenus(Base):
    __tablename__ = "submenus"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
    menu_id = Column(String, ForeignKey("menus.id", ondelete='CASCADE'))
    title = Column(String)
    description = Column(String)

    def response(self, db: Session):
        dishes_count = db.query(Dishes).filter(self.id == Dishes.submenu_id).count()
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "dishes_count": dishes_count
        }


class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(String, primary_key=True, index=True, default=get_uuid)
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
