import os
from appium import webdriver

import pytest

from screens.calculate_screen import CalculationScreen


@pytest.fixture(scope="class")
def driver(request):

    def close_driver():
        driver.quit()

    # driver init code
    app_name = "calculator7.apk"
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))
    print(app_path)

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['app'] = app_path
    desired_caps['newCommandTimeout'] = 300
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    request.addfinalizer(close_driver)
    return driver


@pytest.fixture(scope='class')
def calculate_screen(driver):
    calculate_screen = CalculationScreen(driver)
    calculate_screen.wait_for_pad_disappear()
    return calculate_screen
