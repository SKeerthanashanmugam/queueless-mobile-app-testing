import json
import os
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    config = json.loads((Path(__file__).parent / "config.json").read_text())
    app = os.getenv("QUEUELESS_APP", config.pop("app"))
    server = config.pop("appium_url")
    if app == "CHANGE_TO_ABSOLUTE_APK_PATH":
        pytest.skip("Set QUEUELESS_APP or update automation/config.json with an authorized APK")
    config["app"] = app
    session = webdriver.Remote(server, options=UiAutomator2Options().load_capabilities(config))
    yield session
    session.quit()

