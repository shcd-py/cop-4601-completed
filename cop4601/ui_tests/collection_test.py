from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ButtonTest:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        self.driver = webdriver.Edge(self.driver_path)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def test_buttons(self, url):
        try:
            self.setup()
            self.driver.get(url)
            time.sleep(2)
            self.driver.find_element(By.ID, "doubleClickBtn").click()
            time.sleep(2)
        finally:
            self.teardown()
