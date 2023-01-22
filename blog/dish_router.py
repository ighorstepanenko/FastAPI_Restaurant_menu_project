from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes',
    tags=['Dishes']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_dish(request: schemas.Dishes, db: Session = Depends(get_db)):
    new_dish = models.Dishes(title=request.title, description=request.description)
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish.response()


@router.get('/', status_code=status.HTTP_200_OK)
def all_dishes(db: Session = Depends(get_db)):
    dishes = []
    for dish in db.query(models.Dishes).all():
        dishes.append(dish.response())
    return dishes


@router.get('/{target_dish_id}', status_code=status.HTTP_200_OK, tags=['Dishes'])
def get_dish(target_dish_id, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == target_dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'dish not found')
    return dish.response()


@router.put('/{target_dish_id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowDish)
def update_dish(target_dish_id, request: schemas.Dishes, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == target_dish_id)
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'dish not found')
    dish.update(request)
    db.commit()
    return dish.response()


@router.patch('/{target_dish_id}', status_code=status.HTTP_200_OK)
def update_dish(target_dish_id, request: schemas.Dishes, db: Session = Depends(get_db)):
    dish = db.query(models.Dishes).filter(models.Dishes.id == target_dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'dish not found')
    dish.title = request.title
    dish.description = request.description
    dish.price = request.price
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish.response()


@router.delete('/{target_dish_id}', status_code=status.HTTP_200_OK)
def deleate_dish(target_dish_id, db: Session = Depends(get_db)):
    db.query(models.Dishes).filter(models.Dishes.id == target_dish_id).delete(synchronize_session=False)
    db.commit()
