from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    BUY_BTN = "//button[@data-product-buy-button]"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_buy(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.BUY_BTN)))
        ActionChains(self.driver).move_to_element(btn).click().perform()

    def buy_button_exists(self):
        return len(self.driver.find_elements(By.XPATH, self.BUY_BTN)) > 0