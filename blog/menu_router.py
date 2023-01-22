from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/v1/menus',
    tags=['Menus']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_menu(request: schemas.Menus, db: Session = Depends(get_db)):
    new_menu = models.Menus(title=request.title, description=request.description)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu.response(db)


@router.get('/', status_code=status.HTTP_200_OK)
def all_menus(db: Session = Depends(get_db)):
    menus = []
    for menu in db.query(models.Menus).all():
        menus.append(menu.response(db))
    return menus


@router.get('/{target_menu_id}', status_code=status.HTTP_200_OK)
def get_menu(target_menu_id, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == target_menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    return menu.response(db)


@router.put('/{target_menu_id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowMenu,
            tags=['Menus'])
def update_menu(target_menu_id, request: schemas.Menus, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == target_menu_id)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    menu.update(request)
    db.commit()


@router.patch('/{target_menu_id}', status_code=status.HTTP_200_OK)
def update_menu(target_menu_id, request: schemas.Menus, db: Session = Depends(get_db)):
    menu = db.query(models.Menus).filter(models.Menus.id == target_menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'menu not found')
    menu.title = request.title
    menu.description = request.description
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu.response(db)


@router.delete('/{target_menu_id}', status_code=status.HTTP_200_OK)
def deleate_menu(target_menu_id, db: Session = Depends(get_db)):
    db.query(models.Menus).filter(models.Menus.id == target_menu_id).delete(synchronize_session=False)
    db.commit()
