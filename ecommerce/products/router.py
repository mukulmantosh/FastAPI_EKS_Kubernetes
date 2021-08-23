from typing import List

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ecommerce import db
from . import schema
from . import services

router = APIRouter(
    tags=['Products'],
    prefix='/products'
)


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    return new_category


@router.get('/category', response_model=List[schema.ListCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    return await services.get_all_categories(database)


@router.get('/category/{category_id}', response_model=schema.ListCategory)
async def get_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await services.get_category_by_id(category_id, database)


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_category_by_id(category_id, database)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, database: Session = Depends(db.get_db)):
    product = await services.create_new_product(request, database)
    return product


@router.get('/', response_model=List[schema.ProductListing])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.get_all_products(database)
