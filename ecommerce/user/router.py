from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.auth.jwt import get_current_user
from . import schema
from . import services
from . import validator

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)

# Interesting Question for Global Dependency
# https://github.com/tiangolo/fastapi/issues/2481


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    # Read More : Pydantic Validation with Database (https://github.com/tiangolo/fastapi/issues/979)

    user = await validator.verify_email_exist(request.email, database)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    new_user = await services.new_user_register(request, database)
    return new_user


@router.get('/', response_model=List[schema.DisplayUser])
async def get_all_user(database: Session = Depends(db.get_db), current_user: schema.User = Depends(get_current_user)):
    return await services.all_users(database)


@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                         current_user: schema.User = Depends(get_current_user)):
    return await services.get_user_by_id(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                            current_user: schema.User = Depends(get_current_user)):
    return await services.delete_user_by_id(user_id, database)
