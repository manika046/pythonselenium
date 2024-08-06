#action chains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

element = driver.find_element(By.LINK_TEXT, "Foundational Courses")

action = ActionChains(driver)

action.click(on_element = element)

action.perform()