from product import Product

class CartItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def __repr__(self) -> str:
        return f'CartItem(product={self.product}, quantity={self.quantity})'
