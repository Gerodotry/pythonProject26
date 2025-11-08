from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.e2e
def test_login_valid_credentials(driver, home_page, login_page, credentials):
    wait = WebDriverWait(driver, 10)

    home_page.open()
    login_page.open_login_form()
    login_page.enter_phone(credentials["phone"])
    login_page.enter_password(credentials["password"])
    login_page.submit_login()

    profile_button = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button[data-testid='login']")
        )
    )

    user_name_span = profile_button.find_element(By.CSS_SELECTOR, "span._cjioPkQR")

    assert user_name_span.text.strip() != "", "Ім’я користувача не відображено після входу!"
    print(f" Успішний вхід")
