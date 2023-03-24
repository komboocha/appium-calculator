from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class CalculationScreen:
    # selectors
    pad_selector = (AppiumBy.ID, "pad_advanced")
    digit1_selector = (AppiumBy.ID, 'digit_1')
    digit2_selector = (AppiumBy.ID, 'digit_2')
    digit_1_selector = (AppiumBy.ID, "digit_{value1}")  # add_values3
    digit_2_selector = (AppiumBy.ID, "digit_{value2}")  # add_values3
    digit3_selector = (AppiumBy.ID, 'digit_3')
    minus_sign_selector = (AppiumBy.ID, "op_sub")
    plus_sign_selector = (AppiumBy.ID, "op_add")
    multiply_sign_selector = (AppiumBy.ID, "op_mul")
    divide_sign_selector = (AppiumBy.ID, "op_div")
    equal_sign_selector = (AppiumBy.ID, "eq")
    final_result_selector = (AppiumBy.ID, "result_final")
    sinus_selector = (AppiumBy.ID, "fun_sin")
    arrow_selector = (AppiumBy.ID, "arrow")
    square_root_selector = (AppiumBy.ACCESSIBILITY_ID, "square root")

    def __init__(self, driver):
        self.driver = driver

    def add_values(self):
        self.driver.find_element(*self.digit2_selector).click()
        self.driver.find_element(*self.plus_sign_selector).click()
        self.driver.find_element(*self.digit1_selector).click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def subtract_values(self):
        self.driver.find_element(*self.digit2_selector).click()
        self.driver.find_element(*self.minus_sign_selector).click()
        self.driver.find_element(*self.digit3_selector).click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def multiply_values(self):
        self.driver.find_element(*self.digit2_selector).click()
        self.driver.find_element(*self.multiply_sign_selector).click()
        self.driver.find_element(*self.digit3_selector).click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def divide_values(self):
        self.driver.find_element(*self.digit3_selector).click()
        self.driver.find_element(*self.divide_sign_selector).click()
        self.driver.find_element(*self.digit2_selector).click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def wait_for_pad_disappear(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(self.pad_selector))

    def get_result(self):
        result = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.final_result_selector))
        return result.text

    def add_values2(self, param1, param2):
        self.driver.find_element(AppiumBy.ID, f'digit_{param1}').click()
        self.driver.find_element(*self.plus_sign_selector).click()
        self.driver.find_element(AppiumBy.ID, f'digit_{param2}').click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def subtract_values2(self, param1, param2):
        self.driver.find_element(AppiumBy.ID, f'digit_{param1}').click()
        self.driver.find_element(*self.minus_sign_selector).click()
        self.driver.find_element(AppiumBy.ID, f'digit_{param2}').click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def multiply_values2(self, param1, param2):
        self.driver.find_element(AppiumBy.ID, f'digit_{param1}').click()
        self.driver.find_element(*self.multiply_sign_selector).click()
        self.driver.find_element(AppiumBy.ID, f'digit_{param2}').click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def divide_values2(self, param1, param2):
        self.driver.find_element(AppiumBy.ID, f'digit_{param1}').click()
        self.driver.find_element(*self.divide_sign_selector).click()
        self.driver.find_element(AppiumBy.ID, f'digit_{param2}').click()
        self.driver.find_element(*self.equal_sign_selector).click()

    def add_values3(self, value1, value2):
        self.driver.find_element(self.digit_1_selector[0], self.digit_1_selector[1].format(value1=value1)).click()
        self.driver.find_element(*self.plus_sign_selector).click()
        self.driver.find_element(self.digit_2_selector[0], self.digit_2_selector[1].format(value2=value2)).click()
        self.driver.find_element(*self.equal_sign_selector).click()

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


