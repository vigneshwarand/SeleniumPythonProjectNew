from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.get("https://google.com")

searchBox = driver.find_element_by_name("q")

searchBox.send_keys("Vigneshwaran")

driver.find_element_by_xpath()