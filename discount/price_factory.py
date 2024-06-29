from .pricing_strategies import GroupPricingStrategy, IndividualPricingStrategy
from .base import PricingStrategy


class PricingStrategyFactory:
    @staticmethod
    def create_pricing_strategy(product_name: str) -> PricingStrategy:
        pricing_rules = {
            'A': GroupPricingStrategy(50, 130, 3),
            'B': GroupPricingStrategy(30, 45, 2),
            'C': IndividualPricingStrategy(20),
            'D': IndividualPricingStrategy(15)
        }
        return pricing_rules.get(product_name)
