from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ecommerce import db
from .services import add_to_cart
from ecommerce.user.schema import User
from ecommerce.auth.jwt import get_current_user

router = APIRouter(
    tags=['Cart'],
    prefix='/cart'
)


@router.get('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, current_user: User = Depends(get_current_user),
                              database: Session = Depends(db.get_db)):
    result = await add_to_cart(product_id, current_user, database)
    return result

