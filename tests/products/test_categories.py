import pytest
from httpx import AsyncClient

from ecommerce.products.models import Category
from test_conf import app, override_get_db


@pytest.mark.asyncio
async def test_new_category():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products/category", json={'name': 'Apparels'})
    assert response.status_code == 201
    assert response.json()['name'] == "Apparels"


@pytest.mark.asyncio
async def test_list_get_category():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_category = Category(name="Food")
        database.add(new_category)
        database.commit()
        database.refresh(new_category)
        first_response = await ac.get("/products/category")
        second_response = await ac.get(f"/products/category/{new_category.id}")
    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert second_response.json() == {"id": new_category.id, "name": new_category.name}


@pytest.mark.asyncio
async def test_delete_category():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_category = Category(name="Electronics")
        database.add(new_category)
        database.commit()
        database.refresh(new_category)
        response = await ac.delete(f"/products/category/{new_category.id}")
    assert response.status_code == 204
