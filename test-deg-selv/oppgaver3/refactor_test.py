from refactor import Store, get_total_price

# kjøres med 'pytest' https://docs.pytest.org/en/7.4.x/getting-started.html#get-started


class TestGetTotalPrice:
    def setup_method(self):
        self.store = Store("Test Store", {"salad": 10, "potato": 50})

    def test_buy_one_of_every_product_in_stock(self):
        assert get_total_price(["salad", "potato"], self.store) == 60

    def test_buy_one_product(self):
        assert get_total_price(["salad"], self.store) == 10

    def test_buy_no_products(self):
        assert get_total_price([], self.store) == 0
