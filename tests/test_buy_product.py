import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_buy_first_product():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    home.open()
    time.sleep(2)

    assert home.search_button_exists(), " Кнопка пошуку не знайдена!"
    print(" Кнопка пошуку знайдена")
    home.click_first_product()
    time.sleep(3)

    assert product.buy_button_exists(), " Кнопка 'Купити' не знайдена!"
    print("Кнопка 'Купити' знайдена")

    product.click_buy()
    time.sleep(3)
    assert cart.checkout_button_exists(), " Кнопка Оформити покупку не знайдена!"
    print(" Кнопка 'Оформити покупку' знайдена ")

    driver.quit()
