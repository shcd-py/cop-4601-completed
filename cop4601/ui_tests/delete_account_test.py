from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from ui_tests.login_test import LoginTest

class DeleteAccountTest:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        options = webdriver.EdgeOptions()
        options.binary_location = self.driver_path
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def delete_account(self, base_url, username, password):
        try:
            self.setup()

            # Login işlemini login_test.py'den çağırıyoruz
            login_test = LoginTest(self.driver_path)
            login_test.driver = self.driver  # Mevcut driver'ı kullan
            login_test.login(f"{base_url}/login", username, password)

            # Hesap silme butonuna tıklama
            self.driver.find_element(By.ID, "deleteAccount").click()
            time.sleep(2)

            # Onay penceresindeki "OK" butonuna tıklama
            Alert(self.driver).accept()
            time.sleep(2)
        finally:
            self.teardown()
