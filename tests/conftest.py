import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.search_page import SearchPage


@pytest.fixture(scope="session")
def driver():
    """Ініціалізація WebDriver на всю сесію"""
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # для CI

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def credentials():
    load_dotenv()
    phone = os.getenv("TEST_PHONE")
    password = os.getenv("TEST_PASSWORD")

    assert phone, "Не знайдено TEST_PHONE у .env"
    assert password, "Не знайдено TEST_PASSWORD у .env"
    return {"phone": phone, "password": password}


@pytest.fixture(scope="function")
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture(scope="function")
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture(scope="function")
def search_page(driver):
    return SearchPage(driver)
