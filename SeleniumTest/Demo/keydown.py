#keydown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

action = ActionChains(driver)

action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

