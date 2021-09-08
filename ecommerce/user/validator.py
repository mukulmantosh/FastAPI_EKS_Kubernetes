from typing import Optional

from sqlalchemy.orm import Session

from .models import User


async def verify_email_exist(email: str, db_session: Session) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()
