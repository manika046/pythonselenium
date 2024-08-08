import os
import time

from pathlib import Path
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

env_path = Path('../.venv/.env')
load_dotenv(dotenv_path=env_path)

driver = webdriver.Chrome()

driver.get("https://web.khalti.com/?csrt=2827973035600902215#/")

phone_element = driver.find_element(By.XPATH, "//input[@name= 'id']")
phone_element.send_keys(os.getenv("NUMBER"))

pw_element = driver.find_element(By.XPATH, "//input[@name= 'password']")
pw_element.send_keys(os.getenv("PASSWORD"))

submitbutton = driver.find_element(By.XPATH, "//button[@role='button']")
submitbutton.click()
time.sleep(20)

driver.switch_to.window(driver.current_window_handle)
print(driver.current_url)

topup = driver.find_element(By.XPATH, "//div[@class= 'fundText--1pdtF' and text() = 'Transfer']")
topup.click()

time.sleep(20)

driver.switch_to.window(driver.current_window_handle)
print(driver.current_url)

#for transfer money(khalti to khalti)
khalti_number = driver.find_element(By.XPATH, "//input[@name='user']")
khalti_number.send_keys("9707167505")

transfer_amount = driver.find_element(By.XPATH, "//input[@name='amount']")
transfer_amount.send_keys("10")

submit_button = driver.find_element(By.XPATH, "//button[@class= 'ui primary button']")
submit_button.click()

driver.implicitly_wait(50)

ok_button = driver.find_element(By.XPATH, "//div[@class='ui primary button' and text()='Ok']")
ok_button.click()

# for topup amount
# input_number = driver.find_element(By.XPATH, "//input[@name='number']")
# input_number.send_keys("9707167505")
#
# input_amount = driver.find_element(By.XPATH, "//input[@name='amount']")
# input_amount.send_keys("50")
#
# driver.implicitly_wait(40)
#
# proceed = driver.find_element(By.XPATH, "//div[@class= 'ui primary fluid button mg-top-20' and text()='PROCEED']")
# proceed.click()

time.sleep(50)