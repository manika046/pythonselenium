import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")
# driver.set_window_position(24, 24, windowHandle='current')
# time.sleep(10)

# driver.set_window_rect(x=100, y=200, width=1024, height=700)

#getcurrenturl
# print(driver.current_url)

#getcurrentwindowhandle
# print(driver.current_window_handle)

#getpagesource
print(driver.page_source)