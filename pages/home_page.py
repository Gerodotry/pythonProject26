from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://epicentrk.ua/"
    FIRST_PRODUCT = "/html/body/div/div/div/main/div/div/div[3]/div[2]/div[5]/div/div/ul/li[1]/div/div/a"
    SEARCH_BUTTON = "//button[@aria-label='Пошук']//*[name()='svg']"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def search_button_exists(self):
        return len(self.driver.find_elements(By.XPATH, self.SEARCH_BUTTON)) > 0

    def click_first_product(self):
        product = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_PRODUCT))
        )
        ActionChains(self.driver).move_to_element(product).pause(0.1).click().perform()
