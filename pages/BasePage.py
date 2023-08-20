from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 

class BasePage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 30)
    self.EC = expected_conditions
