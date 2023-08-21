from selenium.webdriver.common.by import By
from . import BasePage
import random

class ItemsPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    
  products_selector = "span[itemprop='name']"
  btn_signin_selector = "span[id='gh-ug']"

  def OpenSignIn(self):
   btn_signin = self.driver.find_element(By.CSS_SELECTOR, self.btn_signin_selector)
   btn_signin.click()
  
  def SelectRandomItem(self):
    products = self.driver.find_elements(By.CSS_SELECTOR, self.products_selector)
    randomProductNumber = random.randint(0, len(products)-1)
    productName = products[randomProductNumber].get_attribute('innerText')
    products[randomProductNumber].click()
    return productName