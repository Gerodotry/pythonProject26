from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://epicentrk.ua/"

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        # Очікуємо появу першого товару саме через ТВОЙ локатор ✅
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@itemtype='https://schema.org/Product']//p[@itemprop='name']/a)[1]")
            )
        )

    @property
    def first_product(self):
        return self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[@itemtype='https://schema.org/Product']//p[@itemprop='name']/a)[1]")
            )
        )

    @property
    def search_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Пошук']//*[name()='svg']")
            )
        )

    def search_button_exists(self):
        try:
            return self.search_button.is_displayed()
        except:
            return False

    def click_first_product(self):
        product = self.first_product
        ActionChains(self.driver).scroll_to_element(product).perform()
        product.click()
