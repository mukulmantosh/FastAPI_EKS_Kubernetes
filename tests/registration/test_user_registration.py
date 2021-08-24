import pytest

from faker import Faker
from httpx import AsyncClient

from test_conf import app


@pytest.mark.asyncio
async def test_registration():
    fake = Faker()
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/user/", json=data)
    assert response.status_code == 201
