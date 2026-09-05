from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Page object for the QueueLess login screen."""

    MOBILE = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    CONTINUE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Continue")',
    )
    OTP = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    VERIFY = (AppiumBy.XPATH, '(//*[@text="Verify OTP"])[last()]',)
    ERROR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter a valid 10-digit mobile number")',)

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def request_otp(self, mobile):
        field = self.wait.until(
            EC.visibility_of_element_located(self.MOBILE)
        )
        field.send_keys(mobile)
        self.driver.find_element(*self.CONTINUE).click()

    def submit_otp(self, otp):
        field = self.wait.until(
            EC.visibility_of_element_located(self.OTP)
        )
        field.send_keys(otp)
        self.driver.find_element(*self.VERIFY).click()

    def error_text(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR)
        )
        return element.text