# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:5000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/demo")
        driver.find_element_by_id("r").clear()
        driver.find_element_by_id("r").send_keys("9543")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

        actual_value = driver.find_element_by_id('result').text
        expected_value = '-0.9161956973220345'
        self.assertEqual(expected_value, actual_value)

    def test_ing(self):
        driver = self.driver
        driver.get(self.base_url + "/demo")
        driver.find_element_by_id("r").clear()
        driver.find_element_by_id("r").send_keys("not number")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

        actual_value = driver.find_element_by_id('result').text
        expected_value = 'Please input number for calculate sine.'
        self.assertEqual(expected_value, actual_value)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
