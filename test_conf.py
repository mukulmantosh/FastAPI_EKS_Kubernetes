import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ecommerce.db import Base, get_db
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


def db_cleanup(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)


engine = create_engine(

    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}

)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_cleanup('test.db')

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
