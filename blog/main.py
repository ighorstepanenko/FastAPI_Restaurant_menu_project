from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session

import database
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/api/v1/menus', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    menus = db.query(models.Menus).all()
    return menus


@app.post('/api/v1/menus', status_code=status.HTTP_201_CREATED)
def create_menu(request: schemas.Menus, db: Session = Depends(get_db)):
    new_menu = models.Menus(title=request.title, description=request.description,
                            submenus_count=request.submenus_count, dishes_count=request.dishes_count)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


@app.get('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_200_OK)
def get_menu(menu_id, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    return menu


@app.put('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_202_ACCEPTED)
def update_menu(menu_id, request: schemas.Menus, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == menu_id)
    if not menu.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    menu.update(request)
    db.commit()


@app.delete('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_204_NO_CONTENT)
def deleate_menu(menu_id, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == menu_id)
    if not menu.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    menu.delete(synchronize_session=False)
    db.commit()


@app.get('/api/v1/menus{target_menu_id}/submenus', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    submenus = db.query(models.Submenus).all()
    return submenus


@app.post('/api/v1/menus/{target_menu_id}/submenus', status_code=status.HTTP_201_CREATED)
def create_submenu(request: schemas.Submenus, db: Session = Depends(get_db)):
    new_submenu = models.Submenus(title=request.title, description=request.description,
                                  dishes_count=request.dishes_count)
    db.add(new_submenu)
    db.commit()
    db.refresh(new_submenu)
    return new_submenu


@app.get('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_200_OK)
def get_submenu(submenu_id, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return submenu


@app.put('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_202_ACCEPTED)
def update_submenu(submenu_id, request: schemas.Submenus, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == submenu_id)
    if not submenu.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    submenu.update(request)
    db.commit()


@app.delete('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_204_NO_CONTENT)
def deleate_submenu(submenu_id, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == submenu_id)
    if not submenu.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    submenu.delete(synchronize_session=False)
    db.commit()


@app.get('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    dishes = db.query(models.Dishes).all()
    return dishes


@app.post('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes', status_code=status.HTTP_201_CREATED)
def create_dish(request: schemas.Dishes, db: Session = Depends(get_db)):
    new_dishes = models.Dishes(title=request.title, description=request.description, price=request.price)
    db.add(new_dishes)
    db.commit()
    db.refresh(new_dishes)
    return new_dishes


@app.get('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
         status_code=status.HTTP_200_OK)
def get_dish(dish_id, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return dish


@app.put('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
         status_code=status.HTTP_202_ACCEPTED)
def update_dish(dish_id, request: schemas.Dishes, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == dish_id)
    if not dish.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    dish.update(request)
    db.commit()


@app.delete('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
            status_code=status.HTTP_204_NO_CONTENT)
def deleate_dish(dish_id, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == dish_id)
    if not dish.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    dish.delete(synchronize_session=False)
    db.commit()
