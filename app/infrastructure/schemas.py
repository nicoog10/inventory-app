def individual_serial_product(product) -> dict:
    return {
        "product_sku" : product["product_sku"],
        "name" : product["name"],
        "description" : product["description"],
        "price" : product["price"],
        "stock" : product["stock"],
        "thumbnail" : product["thumbnail"],
    }
    
def list_serial_product(products) -> list:
    return [individual_serial_product(product) for product in products]

def individual_serial_product_detail(product_detail) -> dict:
    return {
        "product_sku" : product_detail["product_sku"],
        "name" : product_detail["name"],
        "description" : product_detail["description"],
        "price" : product_detail["price"],
        "stock" : product_detail["stock"],
        "images" : product_detail["images"],
    }
    