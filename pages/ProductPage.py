from selenium.webdriver.common.by import By
from . import BasePage

class ProductPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.wait.until(self.EC.url_contains("ebay.com/itm"))

  ddl_color_selector = "select[selectboxlabel='Color']"
  ddl__option_selector = "option[value='2']"
  btn_buy_selector = "div[data-testid='x-bin-action']"
  btn_guest_checkout_selector = "div[class='ux-bin-nudge__guestCheckOut']"

  def ChooseProductOptions(self):
    ddl_color = self.driver.find_element(By.CSS_SELECTOR, self.ddl_color_selector)
    ddl_color.click()
    ddl__option = self.driver.find_element(By.CSS_SELECTOR, self.ddl__option_selector)
    ddl__option.click()

  def BuyProductasGuest(self):
    btn_buy = self.driver.find_element(By.CSS_SELECTOR, self.btn_buy_selector)
    btn_buy.click()
    btn_guest_checkout = self.driver.find_element(By.CSS_SELECTOR, self.btn_guest_checkout_selector)
    btn_guest_checkout.click()