import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

driver = None
home = None
product = None
cart = None
def setup_module():
    global driver, home, product, cart
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
def teardown_module():
    driver.quit()
def test_step1_open_product():
    home.open()
    time.sleep(2)
    home.click_first_product()
    time.sleep(3)
    assert "/ua/shop/" in driver.current_url and driver.current_url.endswith(".html"), \
        " Не потрапили на сторінку товару!"
def test_step2_buy_btn_exists():
    assert product.buy_button_exists(), " Кнопка 'Купити' не знайдена!"
def test_step3_buy_and_checkout_btn():
    product.click_buy()
    time.sleep(5)
    assert cart.checkout_button_exists(), " Кнопка 'Оформити покупку' не знайдена!"
