from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

class ButtonTest:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        service = Service(self.driver_path) 
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=service, options=options)  

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def test_buttons(self, url):
        try:
            self.setup()
            self.driver.get(url)
            time.sleep(2)
            
            action = ActionChains(self.driver)

            # Double click button
            double_click_button = self.driver.find_element(By.ID, "doubleClickBtn")
            action.double_click(double_click_button).perform()
            time.sleep(5)

            # Right click button
            right_click_button = self.driver.find_element(By.ID, "rightClickBtn")
            action.context_click(right_click_button).perform()
            time.sleep(7)

            # Click me button
            click_me_button = self.driver.find_element(By.ID, "Vg4CC")
            click_me_button.click()
            time.sleep(5)
        finally:
            self.teardown()
