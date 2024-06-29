from checkout import Checkout

checkout = Checkout()
products = "A"

for product in products:
    checkout.scan(product)

print(f"Total price: {checkout.total()}")
