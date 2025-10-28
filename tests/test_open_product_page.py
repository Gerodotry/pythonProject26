from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_search_kley():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    driver.get("https://epicentrk.ua/ua/")

    search_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search']"))
    )
    search_input.send_keys("клей")

    search_button_svg = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Пошук']//*[name()='svg']")
        )
    )
    search_button_svg.click()
    print(" Клік по кнопці пошуку виконано!")


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@itemtype='https://schema.org/Product']")
        )
    )
    print(" Результати пошуку завантажені!")

    driver.quit()
