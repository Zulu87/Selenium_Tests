import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class TestWebElements:
    @pytest.mark.wish_shop
    def test_wish_shop_search(self, wish_browser: Chrome):
        search_field = wish_browser.find_element(By.XPATH, "//input[contains(@class, 'form-control input-lg')]")
        search_button = wish_browser.find_element(By.XPATH, "//i[@class = 'fa fa-search']/parent::*")

        search_field.send_keys("Кулон")

        search_button.click()

        found_items = wish_browser.find_elements(By.CSS_SELECTOR, ".product-layout")

        assert len(found_items), "No goods found in a store  "

        for item in found_items:
            assert item.find_element(By.XPATH, "//a"), "No link for items"


    @pytest.mark.wish_shop
    @pytest.mark.parametrize("x_path, media_page",
                            [("//i[contains(@class,'fa-facebook')]", "https://www.facebook.com/brasletgelaniy"),
                            ("//i[contains(@class,'fa-instagram')]", "https://www.instagram.com/braslet_gelaniy/")])
    def test_wish_shop_links(self, wish_browser: Chrome, x_path, media_page):

        shop_media_link = wish_browser.find_element(By.XPATH, x_path)

        shop_media_link.click()

        wish_browser.switch_to.window(wish_browser.window_handles[1])

        assert wish_browser.current_url == media_page, "Some wrong page"
