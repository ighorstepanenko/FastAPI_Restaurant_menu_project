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


@app.post('/api/v1/menus', status_code=status.HTTP_201_CREATED, tags=['Menus'])
def create_menu(request: schemas.Menus, db: Session = Depends(get_db)):
    new_menu = models.Menus(title=request.title, description=request.description)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


@app.get('/api/v1/menus', status_code=status.HTTP_200_OK, tags=['Menus'])
def all_menus(db: Session = Depends(get_db)):
    menus = db.query(models.Menus).all()
    return menus


@app.get('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_200_OK, tags=['Menus'])
def get_menu(target_menu_id, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == target_menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    return menu


@app.put('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowMenu,
         tags=['Menus'])
def update_menu(target_menu_id, request: schemas.Menus, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == target_menu_id)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    menu.update(request)
    db.commit()


@app.patch('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_200_OK, tags=['Menus'])
def update_menu(target_menu_id, request: schemas.Menus, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == target_menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    menu.title = request.title
    menu.description = request.description
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


@app.delete('/api/v1/menus/{target_menu_id}', status_code=status.HTTP_200_OK,
            tags=['Menus'])
def deleate_menu(target_menu_id, db: Session = Depends(get_db)):
    db.query(models.Menus).filter(models.Menus.id == target_menu_id).delete(synchronize_session=False)
    db.commit()


@app.post('/api/v1/menus/{target_menu_id}/submenus', status_code=status.HTTP_201_CREATED, tags=['Submenus'])
def create_menu(request: schemas.Submenus, db: Session = Depends(get_db)):
    new_submenu = models.Submenus(title=request.title, description=request.description)
    db.add(new_submenu)
    db.commit()
    db.refresh(new_submenu)
    return new_submenu


@app.get('/api/v1/menus/{target_menu_id}/submenus', status_code=status.HTTP_200_OK, tags=['Submenus'])
def all_submenus(db: Session = Depends(get_db)):
    submenus = db.query(models.Submenus).all()
    return submenus if submenus else []


@app.get('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_200_OK,
         tags=['Submenus'])
def get_submenu(target_submenu_id, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'submenu not found')
    return submenu


@app.put('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_202_ACCEPTED,
         response_model=schemas.ShowSubmenu, tags=['Submenus'])
def update_submenu(target_submenu_id, request: schemas.Submenus, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id)
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'submenu not found')
    submenu.update(request)
    db.commit()


@app.patch('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_200_OK,
           tags=['Submenus'])
def update_submenu(target_submenu_id, request: schemas.Submenus, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'submenu not found')
    submenu.title = request.title
    submenu.description = request.description
    db.add(submenu)
    db.commit()
    db.refresh(submenu)
    return submenu


@app.delete('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}', status_code=status.HTTP_200_OK,
            tags=['Submenus'])
def deleate_submenu(target_submenu_id, db: Session = Depends(get_db)):
    db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id).delete(synchronize_session=False)
    db.commit()


@app.post('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes', status_code=status.HTTP_201_CREATED,
          tags=['Dishes'])
def create_dish(request: schemas.Dishes, db: Session = Depends(get_db)):
    new_dish = models.Dishes(title=request.title, description=request.description)
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish


@app.get('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes', status_code=status.HTTP_200_OK,
         tags=['Dishes'])
def all_dishes(db: Session = Depends(get_db)):
    dishes = db.query(models.Dishes).all()
    return dishes


@app.get('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
         status_code=status.HTTP_200_OK, tags=['Dishes'])
def get_dish(target_dish_id, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == target_dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'dish not found')
    return dish


@app.put('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
         status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowDish,
         tags=['Dishes'])
def update_dish(target_dish_id, request: schemas.Dishes, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == target_dish_id)
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'dish not found')
    dish.update(request)
    db.commit()


@app.patch('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
           status_code=status.HTTP_200_OK, tags=['Dishes'])
def update_dish(target_dish_id, request: schemas.Dishes, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == target_dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'dish not found')
    dish.title = request.title
    dish.price = request.price
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish


@app.delete('/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
            status_code=status.HTTP_200_OK, tags=['Dishes'])
def deleate_dish(target_dish_id, db: Session = Depends(get_db)):
    db.query(models.Dishes).filter(models.Dishes.id == target_dish_id).delete(synchronize_session=False)
    db.commit()
