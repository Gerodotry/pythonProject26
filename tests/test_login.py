from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_valid_credentials():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open()
    login.open_login_form()
    login.enter_phone("+38 (097) 904-46-37")
    login.enter_password(".WMWAzPp%w,/_6b")
    login.submit_login()

    user_name_span = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[@data-testid='login']//span[contains(normalize-space(),'Павло')]")
        )
    )

    assert "Павло" in user_name_span.text, " Ім’я користувача не з’явилося після входу!"

    driver.quit()
