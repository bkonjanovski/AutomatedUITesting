from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class EcommerceTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_checkout_E2E(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        driver.get("https://www.ebay.com/globaldeals")

        #Select product
        driver.find_elements(By.CSS_SELECTOR, "span[itemprop='name']")[2].click()
        WebDriverWait(driver, 5).until(EC.url_contains("ebay.com/itm"))

        #Complete product details and checkout as guest
        driver.find_element(By.CSS_SELECTOR, "select[selectboxlabel='Color']").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='2']").click()
        driver.find_element(By.CSS_SELECTOR, "div[data-testid='x-bin-action']").click()
        driver.find_element(By.CSS_SELECTOR, "div[class='ux-bin-nudge__guestCheckOut']").click()
        wait.until(EC.url_contains("pay.ebay.com"))

        #Enter customer information
        driver.find_element(By.CSS_SELECTOR, "input[id='lastName']").send_keys("TEST_FIRST_NAME")
        driver.find_element(By.CSS_SELECTOR, "input[id='firstName']").send_keys("TEST_LAST_NAME")
        driver.find_element(By.CSS_SELECTOR, "input[id='addressLine1']").send_keys("TEST_ADDRESS_1")
        driver.find_element(By.CSS_SELECTOR, "input[id='city']").send_keys("TEST_CITY")
        driver.find_element(By.CSS_SELECTOR, "input[id='stateOrProvince']").send_keys("TEST_COUNTRY")
        driver.find_element(By.CSS_SELECTOR, "input[id='postalCode']").clear()
        driver.find_element(By.CSS_SELECTOR, "input[id='postalCode']").send_keys("1234")
        driver.find_element(By.CSS_SELECTOR, "input[id='email']").send_keys("test_email@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='emailConfirm']").send_keys("test_email@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='phoneNumber']").clear() 
        driver.find_element(By.CSS_SELECTOR, "input[id='phoneNumber']").send_keys("70000000")
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='ADD_ADDRESS_SUBMIT']").click()

        #Enter payment information
        WebDriverWait(driver, 5).until_not(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, "section[data-test-id='PAYMENT_METHODS']"), "class", "disabled"))
        driver.find_element(By.CSS_SELECTOR, "input[value='CC']").click()
        driver.find_element(By.CSS_SELECTOR, "input[id='cardNumber']").send_keys("4263 9826 4026 9299")
        driver.find_element(By.CSS_SELECTOR, "input[id='cardExpiryDate']").send_keys("0226")
        driver.find_element(By.CSS_SELECTOR, "input[id='securityCode']").send_keys("837")
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='ADD_CARD']").click()
        wait.until_not(EC.element_attribute_to_include((By.CSS_SELECTOR, "button[data-test-id='CONFIRM_AND_PAY_BUTTON']"), "aria-disabled"))

        #Confirm payment
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='CONFIRM_AND_PAY_BUTTON']").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test-id='NOTIFICATIONS']")))

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    

