from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.auth.jwt import get_current_user
from ecommerce.user.schema import User
from .schema import ShowCart
from .services import add_to_cart, get_all_items, remove_cart_item

router = APIRouter(
    tags=['Cart'],
    prefix='/cart'
)


@router.get('/', response_model=ShowCart)
async def get_all_cart_items(current_user: User = Depends(get_current_user),
                             database: Session = Depends(db.get_db)):
    result = await get_all_items(current_user, database)
    return result


@router.get('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, current_user: User = Depends(get_current_user),
                              database: Session = Depends(db.get_db)):
    result = await add_to_cart(product_id, current_user, database)
    return result


@router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int, current_user: User = Depends(get_current_user),
                                 database: Session = Depends(db.get_db)):
    await remove_cart_item(cart_item_id, current_user, database)
