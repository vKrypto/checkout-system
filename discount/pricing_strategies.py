from .base import PricingStrategy


class GroupPricingStrategy(PricingStrategy):
    def __init__(self, unit_price: float, group_price: float, group_size: int) -> None:
        self.unit_price = unit_price
        self.group_price = group_price
        self.group_size = group_size

    def calculate_price(self, quantity: int) -> float:
        groups = quantity // self.group_size
        remainder = quantity % self.group_size
        return groups * self.group_price + remainder * self.unit_price


class IndividualPricingStrategy(PricingStrategy):
    def __init__(self, price: float) -> None:
        self.price = price

    def calculate_price(self, quantity: int) -> float:
        return self.price * quantity
