from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from ui_tests.login_test import LoginTest

class DeleteAllBooksTest:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        options = webdriver.EdgeOptions()
        options.binary_location = self.driver_path  #edge driver'ın yolu zaten klasör içine gömülü
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def delete_books(self, base_url, username, password):
        try:
            self.setup()

            #def calling
            login_test = LoginTest(self.driver_path)
            login_test.driver = self.driver  
            login_test.login(f"{base_url}/login", username, password)

            #clicking the delete all books button
            self.driver.find_element(By.ID, "deleteAllBooks").click()
            time.sleep(2)

            #clicking the last window writed OK
            Alert(self.driver).accept()
            time.sleep(2)
        finally:
            self.teardown()
