from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    TITLE = (AppiumBy.ACCESSIBILITY_ID, "home-title")
    SEARCH = (AppiumBy.ACCESSIBILITY_ID, "doctor-search")
    RESULT_CARDS = (AppiumBy.ACCESSIBILITY_ID, "doctor-result-card")

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def is_loaded(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).is_displayed()

    def search(self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH))
        field.send_keys(text)
        return self.wait.until(EC.presence_of_all_elements_located(self.RESULT_CARDS))

