import pytest
from selenium.webdriver import Firefox


class TestEbay:

    @pytest.mark.ebay_url_test
    def test_ebay_url(self, ebay_browser: Firefox):
        ebay_url = "https://www.ebay.com/"

        assert ebay_browser.current_url == ebay_url, f"Incorrect URL for the Python site: {ebay_browser.current_url}. Should be: {ebay_url}"