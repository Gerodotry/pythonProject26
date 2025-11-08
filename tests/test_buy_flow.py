from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.e2e
def test_step1_open_product(home_page, driver):
    wait = WebDriverWait(driver, 20)
    home_page.open()
    home_page.click_first_product()
    wait.until(EC.url_matches(r"/ua/shop/.+\.html$"))
    assert "/ua/shop/" in driver.current_url and driver.current_url.endswith(".html"), \
        "Не потрапили на сторінку товару!"
    print("Сторінка товару успішно відкрита.")
@pytest.mark.e2e
def test_step2_buy_btn_exists(product, driver):
    wait = WebDriverWait(driver, 15)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-product-buy-button]")))

    assert product.buy_button_exists(), "Кнопка 'Купити' не знайдена!"

@pytest.mark.e2e
def test_step3_buy_and_checkout_btn(product, cart, driver):
    wait = WebDriverWait(driver, 15)

    product.click_buy()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-cart-product-item]")))

    assert cart.cart_title_exists(), "Кошик не відкрився!"
