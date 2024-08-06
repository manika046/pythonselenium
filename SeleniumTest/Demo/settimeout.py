from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/Fleetpandassh/index.html")

driver.set_page_load_timeout(30)