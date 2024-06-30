import pytest
from .price_factory import PricingStrategyFactory
from .pricing_strategies import GroupPricingStrategy


class TestCreatePricingStrategy:

    def test_returns_group_pricing_strategy_for_product_a(self):
        factory = PricingStrategyFactory()
        strategy = factory.create_pricing_strategy("A")
        assert isinstance(strategy, GroupPricingStrategy)
        assert strategy.unit_price == 50
        assert strategy.group_price == 130
        assert strategy.group_size == 3

    def test_product_name_is_empty_string(self):
        factory = PricingStrategyFactory()
        strategy = factory.create_pricing_strategy("")
        assert strategy is None
