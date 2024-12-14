from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import unittest
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/login/")
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_login_form(self):
        try:
            username = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password = self.wait.until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            
            # Input 
            username.clear()
            username.send_keys("user10")
            password.clear()
            password.send_keys("1")
            
            #submit button
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.TAG_NAME, "button"))
            )
            submit_button.click()
            
            time.sleep(2)
            
            self.wait.until(
                EC.url_to_be("http://127.0.0.1:8000/index.html/topics-detail.html/")
            )
            
            self.assertEqual(
                self.driver.current_url, 
                "http://127.0.0.1:8000/index.html/topics-detail.html/"
            )
                    
        except Exception as e:
            self.driver.save_screenshot("login_test_failure.png")
            print(f"Current URL: {self.driver.current_url}")
            print(f"Error message: {str(e)}")
            raise e
    
    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()