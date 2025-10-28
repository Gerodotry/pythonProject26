from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class LoginPage:
    LOGIN_BUTTON = "//button[@data-testid='login']"
    INPUT_PHONE = "//input[@name='login']"
    INPUT_PASSWORD = "//input[@type='password']"
    SUBMIT_BUTTON = "//button[@data-auth-type='login']"
    ERROR_MESSAGE = "//*[contains(text(),'Невірний') or contains(text(),'помилка')]"

    def __init__(self, driver, timeout=12):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_login_form(self):
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON)))
        ActionChains(self.driver).move_to_element(el).click().perform()
        print("✅ Відкрили форму входу")
        time.sleep(2)

    def enter_phone(self, phone):
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.INPUT_PHONE)))
        field.click()
        field.clear()
        field.send_keys(phone)

    def enter_password(self, password):
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.INPUT_PASSWORD)))
        field.click()
        field.clear()
        field.send_keys(password)

    def submit_login(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON)))
        ActionChains(self.driver).move_to_element(btn).click().perform()

    def error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE)))
            return True
        except TimeoutException:
            return False
