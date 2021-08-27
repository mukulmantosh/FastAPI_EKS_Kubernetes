import pytest
from httpx import AsyncClient

from ecommerce.auth.jwt import create_access_token
from test_conf import app
from tests.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_order_processing():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "john@gmail.com"})
        category_obj = await category_info()
        product_obj = await product_info(category_obj)

        cart_response = await ac.get(f"/cart/add",
                                     params={'product_id': product_obj.id},
                                     headers={'Authorization': f'Bearer {user_access_token}'})

        order_response = await ac.post("/orders/", headers={'Authorization': f'Bearer {user_access_token}'})

    assert cart_response.status_code == 201
    assert order_response.status_code == 201


@pytest.mark.asyncio
async def test_order_listing():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "john@gmail.com"})
        response = await ac.get("/orders/", headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 200
