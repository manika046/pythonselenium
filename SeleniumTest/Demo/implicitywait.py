from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")
myname = driver.find_element(By.ID, "about")