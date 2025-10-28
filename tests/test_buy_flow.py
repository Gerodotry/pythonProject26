def test_step1_open_product(home, driver):
    home.open()
    home.click_first_product()
    assert "/ua/shop/" in driver.current_url and driver.current_url.endswith(".html"), \
        "❌ Не потрапили на сторінку товару!"


def test_step2_buy_btn_exists(product):
    assert product.buy_button_exists(), "❌ Кнопка 'Купити' не знайдена!"


def test_step3_buy_and_checkout_btn(product, cart):
    product.click_buy()
    assert cart.cart_title_exists(), "❌ Кошик не відкрився!"
