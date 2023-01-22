from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/v1/menus/{target_menu_id}/submenus',
    tags=['Submenus']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_submenu(request: schemas.Submenus, db: Session = Depends(get_db)):
    new_submenu = models.Submenus(title=request.title, description=request.description)
    db.add(new_submenu)
    db.commit()
    db.refresh(new_submenu)
    return new_submenu.response(db)


@router.get('/', status_code=status.HTTP_200_OK)
def all_submenus(db: Session = Depends(get_db)):
    submenus = []
    for submenu in db.query(models.Submenus).all():
        submenus.append(submenu.response(db))
    return submenus


@router.get('/{target_submenu_id}', status_code=status.HTTP_200_OK)
def get_submenu(target_submenu_id, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'submenu not found')
    return submenu.response(db)


@router.put('/{target_submenu_id}', status_code=status.HTTP_202_ACCEPTED,
            response_model=schemas.ShowSubmenu)
def update_submenu(target_submenu_id, request: schemas.Submenus, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id)
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'submenu not found')
    submenu.update(request)
    db.commit()


@router.patch('/{target_submenu_id}', status_code=status.HTTP_200_OK)
def update_submenu(target_submenu_id, request: schemas.Submenus, db: Session = Depends(get_db)):
    submenu = db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'submenu not found')
    submenu.title = request.title
    submenu.description = request.description
    db.add(submenu)
    db.commit()
    db.refresh(submenu)
    return submenu.response(db)


@router.delete('/{target_submenu_id}', status_code=status.HTTP_200_OK)
def deleate_submenu(target_submenu_id, db: Session = Depends(get_db)):
    db.query(models.Submenus).filter(models.Submenus.id == target_submenu_id).delete(synchronize_session=False)
    db.commit()
