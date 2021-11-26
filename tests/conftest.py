import pytest as pytest
from selenium.webdriver import Chrome, Firefox, DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def ebay_browser():
    capabilities = DesiredCapabilities.FIREFOX
    firefox_browser = Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=capabilities)
    firefox_browser.maximize_window()
    firefox_browser.get("https://www.ebay.com/")

    yield firefox_browser

    firefox_browser.quit()

@pytest.fixture
def wish_browser():
    chrome_browser = Chrome(executable_path=ChromeDriverManager().install())
    chrome_browser.maximize_window()

    chrome_browser.get("https://wish-shop.com.ua/")

    yield chrome_browser

    chrome_browser.quit()