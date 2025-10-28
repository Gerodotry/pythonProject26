
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://epicentrk.ua/"

    FIRST_PRODUCT = "(//main//li//a[contains(@href,'/p/')])[1]"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def click_first_product(self):
        product = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_PRODUCT))
        )
        ActionChains(self.driver).move_to_element(product).click().perform()
