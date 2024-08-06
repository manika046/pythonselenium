import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")
driver.fullscreen_window()
time.sleep(2)

script = "alert('Alert via selenium')"

driver.execute_script(script)
time.sleep(3)