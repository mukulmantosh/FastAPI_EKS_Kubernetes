import pytest

from httpx import AsyncClient

from test_conf import app


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/login", data={'username': 'john@gmail.com', 'password': 'john123'})
    assert response.status_code == 200


