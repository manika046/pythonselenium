from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

#to print page sources
# print(driver.page_source)

print(driver.title)