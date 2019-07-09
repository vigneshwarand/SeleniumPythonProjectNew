# from selenium import webdriver
#
# import time
#
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
#
# chrome_options.add_argument("--headless")
#
# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="../Drivers/chromedriver.exe")
#
# driver.get("http://www.google.com")
#
# driver.find_element_by_name("q").send_keys("Automation Step by Step")
#
# time.sleep(5)
#
# driver.find_element_by_name("btnK").click()
#
# print(driver.title)
#
# driver.close()
#
# driver.quit()
#
# print("Test Completed")

import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.ie.options import Options

IE_options = webdriver.i

path = "../Drivers/IEDriverServer.exe"

driver = webdriver.Ie(executable_path=path)


driver.get("http://www.google.com")

driver.find_element_by_name("q").send_keys("Automation Step by Step")

time.sleep(5)

driver.find_element_by_name("btnK").click()

print(driver.title)

driver.close()

driver.quit()

print("Test Completed")