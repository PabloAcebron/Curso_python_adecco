from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Escribe aquí tu endpoint

@app.get("/products/{product_id}")
def get_product(product_id:int,include_price:Optional[bool] = False,include_stock:Optional[bool] = False,format:Optional[str] = "summary"):
    
    product_data = {
        "product_id": product_id,
        "name": f"Producto : {product_id}",
        "category" : f"Categoría {product_id % 3 + 1}",
        "format" : format
    }
    
    if include_price:
        product_data["price"] = f"{product_id * 10}.99"
        
    if include_stock:
        product_data["stock"] = {product_id * 5}
    return product_data


# para comprobar usar en el navegador /products/5?include_price=5&include_stock=4&format=basic