from celery import Celery
from fastapi import FastAPI

import config_env as env_var
from ecommerce.auth import router as auth_router
from ecommerce.cart import router as cart_router
from ecommerce.orders import router as order_router
from ecommerce.products import router as product_router
from ecommerce.user import router as user_router

app = FastAPI(title='SAMPLE DOCS')
app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)

celery = Celery(
    __name__,
    broker=f"redis://{env_var.REDIS_HOST}:{env_var.REDIS_PORT}/{env_var.REDIS_DB}",
    backend=f"redis://{env_var.REDIS_HOST}:{env_var.REDIS_PORT}/{env_var.REDIS_DB}"
)
celery.conf.imports = [
    'ecommerce.orders.tasks',
]
