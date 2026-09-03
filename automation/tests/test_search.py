import os
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_search_doctor_by_specialty(driver):
    mobile = os.getenv("QUEUELESS_TEST_MOBILE")
    otp = os.getenv("QUEUELESS_TEST_OTP")
    if not mobile or not otp:
        pytest.skip("Authorized test credentials are not configured")
    LoginPage(driver).request_otp(mobile)
    LoginPage(driver).submit_otp(otp)
    results = HomePage(driver).search("Cardiology")
    assert len(results) > 0

