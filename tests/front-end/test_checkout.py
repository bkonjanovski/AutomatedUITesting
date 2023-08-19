from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from faker import Faker

class EcommerceTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_checkout_E2E(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.ebay.com/globaldeals")
        random_data_generator = Faker()

        #Select product
        driver.find_elements(By.CSS_SELECTOR, "span[itemprop='name']")[2].click()
        wait.until(EC.url_contains("ebay.com/itm"))

        #Complete product details and checkout as guest
        driver.find_element(By.CSS_SELECTOR, "select[selectboxlabel='Color']").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='2']").click()
        driver.find_element(By.CSS_SELECTOR, "div[data-testid='x-bin-action']").click()
        driver.find_element(By.CSS_SELECTOR, "div[class='ux-bin-nudge__guestCheckOut']").click()
        wait.until(EC.url_contains("pay.ebay.com"))

        #Enter customer information
        driver.find_element(By.CSS_SELECTOR, "input[id='lastName']").send_keys(random_data_generator.first_name())
        driver.find_element(By.CSS_SELECTOR, "input[id='firstName']").send_keys(random_data_generator.last_name())
        driver.find_element(By.CSS_SELECTOR, "input[id='addressLine1']").send_keys(random_data_generator.address())
        driver.find_element(By.CSS_SELECTOR, "input[id='city']").send_keys(random_data_generator.city())
        driver.find_element(By.CSS_SELECTOR, "input[id='stateOrProvince']").send_keys(random_data_generator.country())
        driver.find_element(By.CSS_SELECTOR, "input[id='postalCode']").clear()
        driver.find_element(By.CSS_SELECTOR, "input[id='postalCode']").send_keys(random_data_generator.postcode())
        email = random_data_generator.ascii_email()
        driver.find_element(By.CSS_SELECTOR, "input[id='email']").send_keys(email)
        driver.find_element(By.CSS_SELECTOR, "input[id='emailConfirm']").send_keys(email)
        driver.find_element(By.CSS_SELECTOR, "input[id='phoneNumber']").clear() 
        driver.find_element(By.CSS_SELECTOR, "input[id='phoneNumber']").send_keys("70000000")
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='ADD_ADDRESS_SUBMIT']").click()

        #Enter payment information
        WebDriverWait(driver, 5).until_not(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, "section[data-test-id='PAYMENT_METHODS']"), "class", "disabled"))
        driver.find_element(By.CSS_SELECTOR, "input[value='CC']").click()
        driver.find_element(By.CSS_SELECTOR, "input[id='cardNumber']").send_keys(random_data_generator.credit_card_number(card_type='visa16'))
        driver.find_element(By.CSS_SELECTOR, "input[id='cardExpiryDate']").send_keys(random_data_generator.credit_card_expire())
        driver.find_element(By.CSS_SELECTOR, "input[id='securityCode']").send_keys(random_data_generator.credit_card_security_code())
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='ADD_CARD']").click()
        wait.until_not(EC.element_attribute_to_include((By.CSS_SELECTOR, "button[data-test-id='CONFIRM_AND_PAY_BUTTON']"), "aria-disabled"))

        #Confirm payment
        driver.find_element(By.CSS_SELECTOR, "button[data-test-id='CONFIRM_AND_PAY_BUTTON']").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test-id='NOTIFICATIONS']")))

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    

