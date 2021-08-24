import pytest
from httpx import AsyncClient

from test_conf import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}