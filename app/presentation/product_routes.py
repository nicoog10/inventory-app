from fastapi import APIRouter
from app.business_logic import product_service
from app.business_logic.product_model import Product,CreateProduct,UpdateProduct

routes = APIRouter(prefix= '/products', tags=['Product'],)

@routes.get('/hola')
def greet():
    return "Hola integracion continua"

@routes.get('/')
def get_products_by_name(name: str = ""):
    return product_service.find_products_by_name(name)
    
@routes.get('/{sku}/detail')
def get_product_detail_by_sku(sku:str):
    return product_service.find_product_detail_by_sku(sku)
    
@routes.post('/')
def create_product(product:CreateProduct):
    return product_service.create_product(product)

@routes.put('/{sku}')
def update_product(sku:str, product:UpdateProduct):
    return product_service.update_product(sku,product)
    
@routes.delete('/{sku}')
def delete_product_by_sku(sku: str):
    return product_service.delete_product_by_sku(sku)