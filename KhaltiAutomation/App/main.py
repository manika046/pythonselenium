import os
import time
from pathlib import Path
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

env_path=Path('../.venv/.env')
load_dotenv(dotenv_path=env_path)

driver = webdriver.Chrome()

driver.get("https://web.khalti.com/?csrt=2827973035600902215#/")

phoneelement = driver.find_element(By.XPATH, "//input[@name= 'id']")
phoneelement.send_keys(os.getenv("NUMBER"))

pwelement = driver.find_element(By.XPATH, "//input[@name= 'password']")
pwelement.send_keys(os.getenv("PASSWORD"))

submitbutton = driver.find_element(By.XPATH, "//button[@role='button']")
submitbutton.click()
time.sleep(20)

driver.switch_to.window(driver.current_window_handle)
print(driver.current_url)

transfer = driver.find_element(By.XPATH, "//*[@class='FundItem--1yG4v']")
transfer.click()

time.sleep(50)