from typing import Dict
from discount import PricingStrategyFactory
from product import Product


class CartItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"CartItem(product={self.product}, quantity={self.quantity})"


class Cart:
    def __init__(self) -> None:
        self.items: Dict[str, CartItem] = {}

    def add_item(self, product_name: str) -> None:
        if product_name in self.items:
            self.items[product_name].quantity += 1
        else:
            self.items[product_name] = CartItem(Product(product_name, 0), 1)

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items.values():
            strategy = PricingStrategyFactory.create_pricing_strategy(
                item.product.name
            )
            total += strategy.calculate_price(item.quantity)
        return total
