from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    def buy_button(self):
        return self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[data-product-buy-button]"
        )))

    def click_buy(self):
        self.buy_button.click()

    def buy_button_exists(self):
        try:
            self.buy_button  # Якщо не знайде -> TimeoutException
            return True
        except TimeoutException:
            return False
