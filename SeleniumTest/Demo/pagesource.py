from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

print(driver.page_source)