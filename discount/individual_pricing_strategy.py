from .base import PricingStrategy

class IndividualPricingStrategy(PricingStrategy):
    def __init__(self, price: float) -> None:
        self.price = price

    def calculate_price(self, quantity: int) -> float:
        return self.price * quantity
