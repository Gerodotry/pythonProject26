from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:

    def __init__(self, driver, timeout=12):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    def login_button(self):
        return self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[data-testid='login']"
        )))

    @property
    def phone_input(self):
        return self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[name='login']"
        )))

    @property
    def password_input(self):
        return self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[type='password']"
        )))

    @property
    def submit_button(self):
        return self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[data-auth-type='login']"
        )))

    @property
    def error_message(self):
        return self.wait.until(EC.visibility_of_element_located((
            By.XPATH, "//*[contains(text(),'Невірний') or contains(text(),'помилка')]"
        )))

    def open_login_form(self):
        self.login_button.click()

    def enter_phone(self, phone):
        self.phone_input.clear()
        self.phone_input.send_keys(phone)

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def submit_login(self):
        self.submit_button.click()

    def error_displayed(self):
        try:
            self.error_message
            return True
        except TimeoutException:
            return False

    def login_error_visible(self):
        return self.error_displayed()
