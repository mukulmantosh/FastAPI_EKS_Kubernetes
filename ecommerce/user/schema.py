from pydantic import BaseModel, constr, validator, EmailStr

from ecommerce import db
from . import models


class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str


class DisplayUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
