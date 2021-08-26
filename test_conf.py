import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ecommerce.db import Base, get_db
from main import app

import config_env as env_var

DATABASE_USERNAME = env_var.DATABASE_USERNAME
DATABASE_PASSWORD = env_var.DATABASE_PASSWORD
DATABASE_HOST = env_var.DATABASE_HOST
DATABASE_NAME = env_var.TEST_DATABASE_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
