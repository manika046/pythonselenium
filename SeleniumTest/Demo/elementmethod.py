import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")

element = driver.find_element(By.LINK_TEXT, "MENU")

#tocheckelementitvisibletouserornot
# print(element.is_displayed())
# time.sleep(10)

#getproperty
# print(element.get_property('href'))