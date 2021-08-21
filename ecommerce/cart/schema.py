import datetime
from typing import List

from pydantic import BaseModel

from ecommerce.products.schema import Product


class ShowCartItems(BaseModel):
    id: int
    products: Product
    created_date: datetime.datetime

    class Config:
        orm_mode = True


class ShowCart(BaseModel):
    id: int
    cart_items: List[ShowCartItems] = []

    class Config:
        orm_mode = True
