from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_search_kley():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://epicentrk.ua/")
    time.sleep(3)
    search_input = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_input.send_keys("клей")
    time.sleep(1)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Пошук']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_button)
    time.sleep(0.5)
    button_svg = driver.find_element(By.XPATH, "//button[@aria-label='Пошук']//*[name()='svg']")
    ActionChains(driver).move_to_element(button_svg).pause(0.1).click().perform()
    print("✅ Клік по кнопці пошуку виконано!")
    WebDriverWait(driver, 10).until(
        EC.url_contains("/ua/shop/kley/")
    )
    current_url = driver.current_url
    print("🔎 Поточний URL:", current_url)

    assert "/ua/shop/kley/" in current_url, \
        f"❌ Помилка переходу: {current_url}"

    time.sleep(3)
    driver.quit()
