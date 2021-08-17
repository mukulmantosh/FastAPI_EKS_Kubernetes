from fastapi import FastAPI
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router

app = FastAPI(title='SAMPLE DOCS')
app.include_router(user_router.router)
app.include_router(product_router.router)