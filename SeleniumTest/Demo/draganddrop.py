#draganddrop

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

source_element = driver.find_element(By.LINK_TEXT, "Algorithms")

target_element = driver.find_element(By.LINK_TEXT, "What is an Algorithm?")

action = ActionChains(driver)

action.drag_and_drop(source_element, target_element)

action.perform()
