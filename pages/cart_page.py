from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    def cart_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Ваш кошик товарів']")
            )
        )

    def cart_title_exists(self):
        try:
            return self.cart_title.is_displayed()
        except:
            return False
