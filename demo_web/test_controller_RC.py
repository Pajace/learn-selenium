# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re


class test_controller_RC(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://localhost:5000")
        self.selenium.start()

    def test_test_controller__r_c(self):
        sel = self.selenium
        sel.open("/demo")
        sel.type("id=r", "90")
        sel.click("css=input[type=\"submit\"]")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("0.8939966636005579", sel.get_text("id=result"))

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
