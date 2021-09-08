from typing import Optional

from sqlalchemy.orm import Session

from .models import Category


async def verify_category_exist(category_id: int, db_session: Session) -> Optional[Category]:
    return db_session.query(Category).filter(Category.id == category_id).first()
