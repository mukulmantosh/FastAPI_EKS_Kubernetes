import pytest
from httpx import AsyncClient

from ecommerce.products.models import Category, Product
from test_conf import app, override_get_db


@pytest.mark.asyncio
async def test_new_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_category = Category(name="Healthy")
        database.add(new_category)
        database.commit()
        database.refresh(new_category)

        payload = {
            "name": "Quaker Oats",
            "quantity": 4,
            "description": "Quaker: Good Quality Oats",
            "price": 10,
            "category_id": new_category.id
        }

        response = await ac.post("/products/", json=payload)
    assert response.status_code == 201
    assert response.json()['name'] == "Quaker Oats"
    assert response.json()['quantity'] == 4
    assert response.json()['description'] == "Quaker: Good Quality Oats"
    assert response.json()['price'] == int(10)


@pytest.mark.asyncio
async def test_list_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_category = Category(name="Healthy")
        database.add(new_category)
        database.commit()
        database.refresh(new_category)

        payload = {
            "name": "Quaker Oats",
            "quantity": 4,
            "description": "Quaker: Good Quality Oats",
            "price": 10,
            "category_id": new_category.id
        }
        new_product = Product(**payload)
        database.add(new_product)
        database.commit()

        response = await ac.get("/products/")
    assert response.status_code == 200
    assert 'name' in response.json()[0]
    assert 'quantity' in response.json()[0]
    assert 'description' in response.json()[0]
    assert 'price' in response.json()[0]

