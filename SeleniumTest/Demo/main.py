import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('file:///C:/Users/acer/Desktop/Trainne/Day5/Fleetpandassh/app/login.html?Submit=Login')
element = driver.find_element(By.ID, "name")
# element = driver.find_element(By.NAME, "")
# element = driver.find_element(By.XPATH, "name")
element.send_keys("Enter text")

email = driver.find_element(By.ID, "email")
email.send_keys("enter email", Keys.ARROW_DOWN)
time.sleep(10)

print("Success")