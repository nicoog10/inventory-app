from fastapi import FastAPI
from app.presentation.product_routes import routes


app = FastAPI()
app.include_router(routes)