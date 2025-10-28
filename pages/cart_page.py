from selenium.webdriver.common.by import By

class CartPage:
    CHECKOUT_BUTTON = "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def checkout_button_exists(self):
        return len(self.driver.find_elements(By.XPATH, self.CHECKOUT_BUTTON)) > 0
