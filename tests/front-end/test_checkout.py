from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time

class EcommerceTests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_checkout_E2E(self):
        driver = self.driver
        driver.get("https://www.ebay.com/globaldeals")

        #Select product
        driver.find_elements(By.CSS_SELECTOR, "span[itemprop='name']")[2].click()

        #Complete product details and checkout as guest
        driver.find_element(By.CSS_SELECTOR, "select[selectboxlabel='Color']").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='2']").click()
        driver.find_element(By.CSS_SELECTOR, "div[data-testid='x-bin-action']").click()
        driver.find_element(By.CSS_SELECTOR, "div[class='ux-bin-nudge__guestCheckOut']").click()
        time.sleep(5)
        

        #Enter customer information
        driver.refresh()
        driver.find_element(By.CSS_SELECTOR, "input[id='lastName']").send_keys("TEST_FIRST_NAME")
        driver.find_element(By.CSS_SELECTOR, "input[id='firstName']").send_keys("TEST_LAST_NAME")
        driver.find_element(By.CSS_SELECTOR, "input[id='addressLine1']").send_keys("TEST_ADDRESS_1")
        driver.find_element(By.CSS_SELECTOR, "input[id='city']").send_keys("TEST_CITY")
        driver.find_element(By.CSS_SELECTOR, "input[id='stateOrProvince']").send_keys("TEST_COUNTRY")
        driver.find_element(By.CSS_SELECTOR, "input[id='postalCode']").send_keys("1234")
        driver.find_element(By.CSS_SELECTOR, "input[id='email']").send_keys("test_email@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='emailConfirm']").send_keys("test_email@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='phoneNumber']").send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
        driver.find_element(By.CSS_SELECTOR, "input[id='phoneNumber']").send_keys("70000000")
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='ADD_ADDRESS_SUBMIT']").click()
        time.sleep(5)

        #Enter payment information
        driver.find_element(By.CSS_SELECTOR, "input[value='CC']").click()
        driver.find_element(By.CSS_SELECTOR, "input[id='cardNumber']").send_keys("4263 9826 4026 9299")
        driver.find_element(By.CSS_SELECTOR, "input[id='cardExpiryDate']").send_keys("0226")
        driver.find_element(By.CSS_SELECTOR, "input[id='securityCode']").send_keys("837")
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='ADD_CARD']").click()
        time.sleep(5)

        #Confirm payment
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='CONFIRM_AND_PAY_BUTTON']").click()
        time.sleep(10)

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    

