import unittest
from selenium import webdriver

import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation step by step - Google Search")

    def test_search2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Vignesh")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Vignesh - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PycharmProjects/Selenium/First_Selenium/Reports'),verbosity=2)
    # unittest.main(verbosity=2)
