from fastapi import FastAPI

from product import ProductList
from checkout import Checkout

app = FastAPI()


@app.post("/checkout")
def checkout(product_list: ProductList):
    checkout = Checkout()
    for product in product_list.products:
        checkout.scan(product)
    return {"total_price": checkout.total()}
