from typing import Optional

from pydantic import BaseModel, constr


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


class ProductListing(ProductBase):
    category: ListCategory

    class Config:
        orm_mode = True
