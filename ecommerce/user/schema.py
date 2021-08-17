from pydantic import BaseModel, constr, validator, EmailStr

from ecommerce import db
from . import models


class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str

    @validator('email')
    def email_must_be_unique(cls, e):
        # When you get the error AttributeError: 'generator'
        # object has no attribute 'query' python is telling you that
        # the result of get_db() is not an sqlalchemy session
        # object but rather a generator that yields a session object.

        database = next(db.get_db())

        email_exist = database.query(models.User).filter(models.User.email == e).count()
        if email_exist:
            raise ValueError('email already taken')
        return e


class DisplayUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
