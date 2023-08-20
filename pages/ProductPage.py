from selenium.webdriver.common.by import By
from . import BasePage
from selenium.webdriver.support.ui import Select

class ProductPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.wait.until(self.EC.url_contains("ebay.com/itm"))

  ddl_options_selector = "select[class='x-msku__select-box']"
  ddl__valid_option_selector = "option:not([disabled], [value='-1'])"
  btn_buy_selector = "div[data-testid='x-bin-action']"
  btn_add_to_cart_selector = "div[data-testid='x-atc-action']"
  btn_guest_checkout_selector = "div[class='ux-bin-nudge__guestCheckOut']"

  def ChooseProductOptionsIfApplicable(self):
    ddl_options = self.driver.find_elements(By.CSS_SELECTOR, self.ddl_options_selector)
    for ddl_option in ddl_options:
      valid_option = ddl_option.find_elements(By.CSS_SELECTOR, self.ddl__valid_option_selector)[0]
      select = Select(ddl_option)
      select.select_by_value(valid_option.get_attribute("value"))

  def BuyProductasGuest(self):
    btn_buy = self.driver.find_element(By.CSS_SELECTOR, self.btn_buy_selector)
    btn_buy.click()
    btn_guest_checkout = self.driver.find_element(By.CSS_SELECTOR, self.btn_guest_checkout_selector)
    btn_guest_checkout.click()

  def AddProductToCart(self):
    productLink = self.driver.current_url.split("?")[0]
    btn_add_to_cart = self.driver.find_element(By.CSS_SELECTOR, self.btn_add_to_cart_selector)
    btn_add_to_cart.click()
    return productLink
  