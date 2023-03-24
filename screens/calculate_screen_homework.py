from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class CalculationScreen:

    pad_selector = (AppiumBy.ID, "pad_advanced")
    digit_1_selector = (AppiumBy.ID, "digit_{value1}")
    equal_sign_selector = (AppiumBy.ID, "eq")
    final_result_selector = (AppiumBy.ID, "result_final")
    sinus_selector = (AppiumBy.ID, "fun_sin")
    arrow_selector = (AppiumBy.ID, "arrow")
    square_root_selector = (AppiumBy.ACCESSIBILITY_ID, "square root")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_pad_disappear(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(self.pad_selector))

    def get_result(self):
        result = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.final_result_selector))
        return result.text

    def open_panel(self):
        actions = TouchAction(self.driver)
        actions.tap(x=1024, y=1024)
        actions.perform()

    def close_panel(self):
        self.driver.find_element(*self.arrow_selector).click()

    def sinus_method(self, value):
        self.open_panel()
        self.driver.find_element(*self.sinus_selector).click()
        self.close_panel()
        self.driver.find_element(self.digit_1_selector[0], self.digit_1_selector[1].format(value1=value)).click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def calculate_root(self, value):
        self.open_panel()
        self.driver.find_element(*self.square_root_selector).click()
        self.close_panel()
        self.driver.find_element(self.digit_1_selector[0], self.digit_1_selector[1].format(value1=value)).click()
        self.driver.find_element(*self.equal_sign_selector).click()