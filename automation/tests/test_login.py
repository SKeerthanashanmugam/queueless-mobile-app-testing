import os

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_invalid_mobile_shows_validation(driver):
    login = LoginPage(driver)
    login.request_otp("12345")
    assert login.error_text()


def test_valid_test_otp_login(driver):
    mobile = os.getenv("QUEUELESS_TEST_MOBILE")
    otp = os.getenv("QUEUELESS_TEST_OTP")
    if not mobile or not otp:
        import pytest
        pytest.skip("Authorized test mobile/OTP environment variables are not configured")
    login = LoginPage(driver)
    login.request_otp(mobile)
    login.submit_otp(otp)
    assert HomePage(driver).is_loaded()

