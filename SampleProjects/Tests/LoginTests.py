import time
import unittest
from selenium import webdriver

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from SampleProjects.Pages.LoginPage1 import LoginPage1
from SampleProjects.Pages.HomePage1 import HomePage1

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valod(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage1(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        homepage = HomePage1(driver)
        homepage.click_welcome()
        homepage.click_logout()
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
