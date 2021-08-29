import pytest
from httpx import AsyncClient

from ecommerce.auth.jwt import create_access_token
from conf_test_db import app
from tests.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_add_to_cart():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        category_obj = await category_info()
        product_obj = await product_info(category_obj)
        user_access_token = create_access_token({"sub": "john@gmail.com"})

        response = await ac.get(f"/cart/add",
                                params={'product_id': product_obj.id},
                                headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 201
    assert response.json() == {"status": "Item Added to Cart"}


@pytest.mark.asyncio
async def test_cart_listing():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "john@gmail.com"})

        response = await ac.get(f"/cart/", headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 200
