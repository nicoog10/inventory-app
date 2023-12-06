
from app.business_logic.product_model import Product,CreateProduct,UpdateProduct
from app.infrastructure.db_connection import product_collection
from app.infrastructure.schemas import list_serial_product , individual_serial_product , individual_serial_product_detail

def find_products_by_name(name:str):
    products = list_serial_product(product_collection.find({"name":{"$regex": name, "$options": "i"}}))
    return products

def find_product_detail_by_sku(sku:str):
    return individual_serial_product_detail(product_collection.find_one({"product_sku":sku}))
    
def create_product(product:CreateProduct):
    product_collection.insert_one(dict(product))
    return product

def update_product(sku:str, product:UpdateProduct):
    return individual_serial_product(product_collection.find_one_and_update({"product_sku":sku},{"$set":product.model_dump(exclude_unset=True)}))

def delete_product_by_sku(sku:str):
    return individual_serial_product(product_collection.find_one_and_delete({"product_sku":sku}))