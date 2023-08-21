from selenium.webdriver.common.by import By
from . import BasePage
from faker import Faker

class SigninPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.wait.until(self.EC.url_contains("signin.ebay.com"))

  input_username_selector = "input[id='userid']" 
  btn__submit_login_selector = "button[id='signin-continue-btn']"
  error_message_selector = "p[id='signin-error-msg']"
  btn_fb_login_selector = "btn[id='signin_fb_btn']"

  def EnterInvalidLogin(self):
      input_username = self.driver.find_element(By.CSS_SELECTOR, self.input_username_selector)
      input_username.send_keys(Faker().ascii_email())

  def SubmitLogin(self):
      btn__submit_login = self.driver.find_element(By.CSS_SELECTOR, self.btn__submit_login_selector)
      btn__submit_login.click()

  def VerifyFacebookLoginRedirection(self):
      btn_fb_login = self.driver.find_element(By.CSS_SELECTOR, self.btn_fb_login_selector)
      btn_fb_login.click()
      self.wait.until(self.EC.url_contains("facebook.com"))

  def VerifyLoginError(self):
    self.wait.until(self.EC.presence_of_element_located((By.CSS_SELECTOR, self.error_message_selector)))


  