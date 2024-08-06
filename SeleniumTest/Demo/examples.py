import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Example(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearch(self):
        driver = self.driver
        driver.get("http://www.python.org/")
        self.assertIn("Python", driver.title)

        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source

    def tearDown(self):
        # self.driver.close()
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
