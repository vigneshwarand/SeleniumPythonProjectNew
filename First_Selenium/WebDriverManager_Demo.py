import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager("2.36").install())

driver.get("https://google.com")

time.sleep(2)

driver.close()

driver.quit()