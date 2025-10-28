import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_invalid_credentials():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    home = HomePage(driver)
    login = LoginPage(driver)
    home.open()
    time.sleep(2)
    login.open_login_form()
    time.sleep(2)
    login.enter_phone("+38 (097) 904-46-37")
    login.enter_password(".WMWAzPp%w,/_6b")
    time.sleep(1)
    login.submit_login()
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    user_name_xpath = "/html/body/div/div/div/div[1]/header/div/div[1]/div[6]/div/button/span[2]"
    try:
        user_name = wait.until(
            EC.visibility_of_element_located((By.XPATH, user_name_xpath))
        )
        print(" Ім’я:", user_name.text)
    except:
        raise AssertionError("❌ Не знайдено ім’я користувача після входу!")

    driver.quit()
