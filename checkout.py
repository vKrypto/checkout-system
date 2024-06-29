from cart import Cart


class Checkout:
    def __init__(self) -> None:
        self.cart = Cart()

    def scan(self, product_name: str) -> None:
        self.cart.add_item(product_name)

    def total(self) -> float:
        return self.cart.calculate_total()
