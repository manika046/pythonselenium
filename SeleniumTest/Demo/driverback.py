import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")
time.sleep(5)

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html#about")
time.sleep(5)

driver.back()