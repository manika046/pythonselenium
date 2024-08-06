# CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, "nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()