from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../Drivers/chromedriver.exe")
# driver.implicitly_wait(10)

driver.get("https://google.com")

driver.find_element_by_name("q").send_keys("Automation")

try:
    wait = WebDriverWait(driver,10)
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
except:
    print("Element is not clickable")
    exit(1)
print("Elemet is Clickable")

element.click()

# driver.find_element_by_name("btnK").click()

print("Test Completed")

driver.close()

driver.quit()