from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from ecommerce import db
from . import models
from . import schema

router = APIRouter(
    tags=['Products'],
    prefix='/products'
)


@router.post('/category', status_code=status.HTTP_201_CREATED)
def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


@router.get('/category', response_model=List[schema.ListCategory])
def get_all_categories(database: Session = Depends(db.get_db)):
    categories = database.query(models.Category).all()
    return categories


@router.get('/category/{category_id}', response_model=schema.ListCategory)
def get_user_by_id(category_id: int, database: Session = Depends(db.get_db)):
    category_info = database.query(models.Category).get(category_id)
    if not category_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return category_info


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_user_by_id(category_id: int, database: Session = Depends(db.get_db)):
    database.query(models.Category).filter(models.Category.id == category_id).delete()
    database.commit()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_product(request: schema.Product, database: Session = Depends(db.get_db)):
    new_product = models.Product(name=request.name, quantity=request.quantity,
                                 description=request.description, price=request.price,
                                 category_id=request.category_id)
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


@router.get('/', response_model=List[schema.ProductListing])
def get_all_products(database: Session = Depends(db.get_db)):
    products = database.query(models.Product).all()
    return products
