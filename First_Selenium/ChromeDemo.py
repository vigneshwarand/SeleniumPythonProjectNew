# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
#
# chrome_options.add_argument("--headless")
#
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../Drivers/chromedriver.exe")
#
# driver.get("https://google.com")
#
# print(driver.title)
#
# driver.close()
#
# driver.quit()
#
# print("Test Completed")



from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../Drivers/chromedriver.exe")

driver.get("https://google.com")

print(driver.title)

driver.close()

driver.quit()

print("Test Completed")