from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
@pytest.mark.e2e
def test_search_kley(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://epicentrk.ua/ua/")

    search_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-ui-input][type='search']"))
    )
    search_input.clear()
    search_input.send_keys("клей")

    search_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Пошук']"))
    )
    search_button.click()

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "a[data-category-link='true'][title*='Клей']")
        )
    )

    assert any("клей" in p.text.lower() for p in products), "Не знайдено товарів із 'клей'"
    print(f"✅ Знайдено {len(products)} товарів зі словом 'клей'")
