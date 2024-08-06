import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://automationstepbystep.com/")

#getcookies
# print(driver.get_cookies())

#get_log
# driver.get_log("browser")
# time.sleep(50)

#getscreenshotasbase64
# print(driver.get_screenshot_as_base64())

#getscreenshotasfile
# print(driver.get_screenshot_as_file("foo.png"))

#getscreenshotaspng
# print(driver.get_screenshot_as_png())

#getwindowposition
# print(driver.get_window_position(windowHandle ='current'))

#getwindowrect
# print(driver.get_window_rect())

#getwindowsize
# print(driver.get_window_size())