from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Replace example accessibility IDs after inspecting the authorized app build."""

    MOBILE = (AppiumBy.ACCESSIBILITY_ID, "mobile-number")
    CONTINUE = (AppiumBy.ACCESSIBILITY_ID, "continue-button")
    OTP = (AppiumBy.ACCESSIBILITY_ID, "otp-input")
    VERIFY = (AppiumBy.ACCESSIBILITY_ID, "verify-otp-button")
    ERROR = (AppiumBy.ACCESSIBILITY_ID, "validation-error")

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def request_otp(self, mobile):
        field = self.wait.until(EC.visibility_of_element_located(self.MOBILE))
        field.send_keys(mobile)
        self.driver.find_element(*self.CONTINUE).click()

    def submit_otp(self, otp):
        self.wait.until(EC.visibility_of_element_located(self.OTP)).send_keys(otp)
        self.driver.find_element(*self.VERIFY).click()

    def error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR)).text

