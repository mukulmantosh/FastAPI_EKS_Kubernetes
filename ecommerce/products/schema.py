from typing import List, Optional

from pydantic import BaseModel, constr, validator

from ecommerce import db
from . import models


class Category(BaseModel):
    name: constr(min_length=2, max_length=50)


class ListCategory(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    quantity: int
    description: str
    price: float

    class Config:
        orm_mode = True


class Product(ProductBase):
    category_id: int

    @validator('category_id')
    def check_category_exist(cls, e):
        # When you get the error AttributeError: 'generator'
        # object has no attribute 'query' python is telling you that
        # the result of get_db() is not an sqlalchemy session
        # object but rather a generator that yields a session object.

        database = next(db.get_db())

        category_exist = database.query(models.Category).filter(models.Category.id == e).count()
        if not category_exist:
            raise ValueError('Invalid Category ID')
        return e


class ProductListing(ProductBase):
    category: ListCategory

    class Config:
        orm_mode = True
