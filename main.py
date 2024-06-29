from checkout import Checkout

checkout = Checkout()
products = "AAABBD"

for product in products:
    checkout.scan(product)

print(f"Total price: {checkout.total()}")
