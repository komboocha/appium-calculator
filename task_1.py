import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Returns abs path relative to this file and not cwd
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

app_name = "calculator7.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))
print(app_path)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['app'] = app_path
desired_caps['newCommandTimeout'] = 300

# desired_caps['platformVersion'] = '10'
# desired_caps['deviceName'] = 'Android Emulator'

#
#
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element(AppiumBy.ID, "digit_2").click()

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "degree mode").click()

degree_radian_selector = (AppiumBy.ACCESSIBILITY_ID, "degree mode")
degree_radian_button = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable(degree_radian_selector))
degree_radian_button.click()


final_result = driver.find_element(AppiumBy.ID, "final_result")
assert final_result.text == 5
