from selenium.webdriver.common.by import By
from . import BasePage

class ItemsPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    
  products_selector = "span[itemprop='name']"

  def SelectRandomItem(self):
    products = self.driver.find_elements(By.CSS_SELECTOR, self.products_selector)
    products[2].click()