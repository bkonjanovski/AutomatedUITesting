from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker
from . import BasePage

class CheckoutPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.wait.until(self.EC.url_contains("pay.ebay.com"))

  ddl_country_selector = "select[id='country']"
  input_first_name_selector = "input[id='firstName']"
  input_last_name_selector = "input[id='lastName']"
  input_address1_selector = "input[id='addressLine1']"
  input_city_selector = "input[id='city']"
  input_state_selector = "input[id='stateOrProvince']"
  input_postal_selector = "input[id='postalCode']"
  input_email_selector = "input[id='email']"
  input_email_confirm_selector = "input[id='emailConfirm']"
  input_phone_number_selector = "input[id='phoneNumber']"
  btn_done_customer_information_selector = "button[data-test-id='ADD_ADDRESS_SUBMIT']"
  section_payment_methods_selector = "section[data-test-id='PAYMENT_METHODS']"
  radio_payment_method_CC_selector = "input[value='CC']"
  radio_payment_method_paypal_selector = "input[value='PAYPAL']"
  input_card_number_selector = "input[id='cardNumber']"
  input_expiry_date_selector = "input[id='cardExpiryDate']"
  input_security_code_selector = "input[id='securityCode']"
  btn_add_card_selector = "button[data-test-id='ADD_CARD']"
  btn_pay_paypal_selector = "button[class='paypal-button-internal--container paypal']"
  section_paypal_login_selector = "p[aria-label='PayPal Logo']"
  btn_confirm_and_pay_selector = "button[data-test-id='CONFIRM_AND_PAY_BUTTON']"
  section_notificiations_selector = "div[data-test-id='NOTIFICATIONS']"
  
  def EnterRandomCustomerInformation(self):
    country = Select(self.driver.find_element(By.CSS_SELECTOR, self.ddl_country_selector))
    country.select_by_visible_text("Macedonia")
    self.driver.find_element(By.CSS_SELECTOR, self.input_first_name_selector).send_keys(Faker().first_name())
    self.driver.find_element(By.CSS_SELECTOR, self.input_last_name_selector).send_keys(Faker().last_name())
    self.driver.find_element(By.CSS_SELECTOR, self.input_address1_selector).send_keys(Faker().address())
    self.driver.find_element(By.CSS_SELECTOR, self.input_city_selector).send_keys(Faker().city())
    self.driver.find_element(By.CSS_SELECTOR, self.input_state_selector).send_keys(Faker().country())
    self.driver.find_element(By.CSS_SELECTOR, self.input_postal_selector).clear()
    self.driver.find_element(By.CSS_SELECTOR, self.input_postal_selector).send_keys(Faker().postcode())
    email = Faker().ascii_email()
    self.driver.find_element(By.CSS_SELECTOR, self.input_email_selector).send_keys(email)
    self.driver.find_element(By.CSS_SELECTOR, self.input_email_confirm_selector).send_keys(email)
    self.driver.find_element(By.CSS_SELECTOR, self.input_phone_number_selector).clear() 
    self.driver.find_element(By.CSS_SELECTOR, self.input_phone_number_selector).send_keys("70000000")
    self.driver.find_element(By.CSS_SELECTOR, self.btn_done_customer_information_selector).click()
    self.wait.until_not(self.EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, self.section_payment_methods_selector), "class", "disabled"))

  def EnterCCaymentInformation(self, cc_number = Faker().credit_card_number(card_type='visa16'), cc_expire = Faker().credit_card_expire(), cc_cvv = Faker().credit_card_security_code()):
    self.driver.find_element(By.CSS_SELECTOR, self.radio_payment_method_CC_selector).click()
    self.driver.find_element(By.CSS_SELECTOR, self.input_card_number_selector).send_keys(cc_number)
    self.driver.find_element(By.CSS_SELECTOR, self.input_expiry_date_selector).send_keys(cc_expire)
    self.driver.find_element(By.CSS_SELECTOR, self.input_security_code_selector).send_keys(cc_cvv)
    self.driver.find_element(By.CSS_SELECTOR, self.btn_add_card_selector).click()

  def VerifyPaymentError(self):
    self.wait.until(self.EC.presence_of_element_located((By.CSS_SELECTOR, self.section_notificiations_selector)))

  def EnterPayPalPaymentInformation(self):
    self.driver.find_element(By.CSS_SELECTOR, self.radio_payment_method_paypal_selector).click()
    self.driver.find_element(By.CSS_SELECTOR, self.btn_pay_paypal_selector).click()
    self.wait.until(self.EC.url_contains("paypal.com"))
    self.wait.until(self.EC.presence_of_element_located((By.CSS_SELECTOR, self.section_paypal_login_selector)))

  def ConfirmOrder(self):
    self.wait.until_not(self.EC.element_attribute_to_include((By.CSS_SELECTOR, self.btn_confirm_and_pay_selector), "aria-disabled"))
    self.driver.find_element(By.CSS_SELECTOR, self.btn_confirm_and_pay_selector).click()
    self.wait.until(self.EC.presence_of_element_located((By.CSS_SELECTOR, self.section_notificiations_selector)))
