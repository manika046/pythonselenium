

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")
element = driver.find_element(By.LINK_TEXT, "MENU")

action = ActionChains(driver)

action.click_and_hold(on_element = element)

action.perform()
