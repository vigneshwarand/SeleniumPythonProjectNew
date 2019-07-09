from selenium import webdriver

import time

path = "../Drivers/geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)

driver.get("https://google.com")

time.sleep(5)

print(driver.title)

driver.close()

driver.quit()
