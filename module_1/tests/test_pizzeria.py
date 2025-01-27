import time
import pytest


class TestPizzeria:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.webdriver = driver

    def test_open_page(self):
        self.webdriver.get('http://pizzeria.skillbox.cc/about/')
        time.sleep(5)
