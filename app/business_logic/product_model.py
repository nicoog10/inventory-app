

from typing import Optional
from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    product_sku : str
    name : str
    description : str
    price : int
    stock : int
    thumbnail : str
    images : list[str]
    
class UpdateProduct(BaseModel):
    name : Optional[str] = Field(None)
    description : Optional[str] = Field(None)
    price : Optional[int] = Field(None)
    stock : Optional[int] = Field(None)
    thumbnail : Optional[str] = Field(None)
    images : Optional[list[str]] = Field(None)
 
class Product(BaseModel):
    product_sku : str
    name : str
    description : str
    price : int
    stock : int
    thumbnail : str
    
class ProductDetail(BaseModel):
    product_sku : str
    name : str
    description : str
    price : int
    stock : int
    images : list[str]
    

