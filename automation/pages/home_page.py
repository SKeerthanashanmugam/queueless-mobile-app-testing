from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Find a Doctor")',)
    SEARCH = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    RESULT_CARDS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Cardiology")',
    )

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def is_loaded(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).is_displayed()

    def search(self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH))
        field.send_keys(text)
        return self.wait.until(EC.presence_of_all_elements_located(self.RESULT_CARDS))

