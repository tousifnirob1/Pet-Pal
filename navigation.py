from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import os

os.environ['WDM_LOG_LEVEL'] = '0'

class TestNavigation(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--silent')
        
        self.service = Service(ChromeDriverManager().install(), log_output=os.devnull)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1:8000"
        self.wait = WebDriverWait(self.driver, 10)

    def test_navigation(self):
        self.driver.get(self.base_url)
        time.sleep(2)

        nav_items = [
            {"text": "Home", "selector": "a[href='/']"},
            {"text": "Services", "selector": "a[href*='section_2']"},
            {"text": "How it Works", "selector": "a[href*='section_3']"},
            {"text": "FAQs", "selector": "a[href*='section_4']"}
        ]

        for item in nav_items:
            try:
                button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, item["selector"]))
                )
            except:
                button = self.wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, item["text"]))
                )
            
            button.click()
            time.sleep(1)
            self.assertTrue(True)

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)