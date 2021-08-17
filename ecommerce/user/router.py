from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from ecommerce import db
from . import models
from . import schema

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


@router.get('/', response_model=List[schema.DisplayUser])
def get_all_user(database: Session = Depends(db.get_db)):
    users = database.query(models.User).all()
    return users


@router.get('/{user_id}', response_model=schema.DisplayUser)
def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return user_info


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
