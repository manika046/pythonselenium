import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.venv/.env')
load_dotenv(dotenv_path=dotenv_path)

driver = webdriver.Chrome()

driver.get("http://www.facebook.com")

user_box = driver.find_element(By.ID, "email")
user_box.send_keys(os.getenv("USER_ID"))

password_box = driver.find_element(By.ID, "pass")
password_box.send_keys(os.getenv("PASSWORD"))

login_box = driver.find_element(By.NAME, "login")
login_box.click()

print("LogIn Successful")

time.sleep(20)
