import time

from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://google.com")

driver.find_element_by_name("q").send_keys("Automation Step by Step")

time.sleep(10)

driver.find_element_by_name("btnK").click()

time.sleep(2)

driver.close()

driver.quit()

print("Test Completed")