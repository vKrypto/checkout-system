import pytest
from checkout import Checkout


class TestCheckoutClass:

    @pytest.mark.parametrize(
        "items, expected_total",
        [
            ("", 0.0),
            ("A", 50.0),
            ("AB", 80.0),
            ("CDBA", 115.0),
            ("AA", 100.0),
            ("AAA", 130.0),
            ("AAAA", 180.0),
            ("AAAAA", 230.0),
            ("AAAAAA", 260.0),
            ("AAAB", 160.0),
            ("AAABB", 175.0),
            ("AAABBD", 190.0),
            ("DABABA", 190.0),
        ],
    )
    def test_checkout(self, items, expected_total):
        checkout = Checkout()
        for item in items:
            checkout.scan(item)
        assert (
            checkout.total() == expected_total
        ), f"Failed for input {items}: expected {expected_total}, got {checkout.total()}"
        print(f"Passed for input {items}: total = {checkout.total()}")

    def test_scan_adds_product_to_cart(self, mocker):
        mock_cart = mocker.patch("checkout.models.Cart")
        checkout = Checkout()
        checkout.scan("ABB")
        mock_cart.return_value.add_item.assert_called_once_with("ABB")

    def test_scan_handles_empty_product_name(self, mocker):
        mock_cart = mocker.patch("checkout.models.Cart")
        checkout = Checkout()
        checkout.scan("")
        mock_cart.return_value.add_item.assert_called_once_with("")
