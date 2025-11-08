from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    URL = "https://epicentrk.ua/"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    def first_product(self):
        return self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//main//li//a[contains(@href,'/p/')])[1]"
        )))

    def open(self):
        self.driver.get(self.URL)

    def click_first_product(self):
        self.first_product.click()
