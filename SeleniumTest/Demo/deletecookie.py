import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")

driver.add_cookie({"name": "minie", "value": "boo"})

driver.delete_cookie("minie")
time.sleep(25)