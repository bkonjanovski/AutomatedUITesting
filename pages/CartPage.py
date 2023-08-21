from selenium.webdriver.common.by import By
from . import BasePage

class CartPage(BasePage.BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.wait.until(self.EC.url_contains("cart.payments.ebay"))

  section_cart_selector = "div[data-test-id='app-cart']"
  cart_icon_selector = "i[id='gh-cart-n']"
  btn_remove_from_cart_selector = "button[data-test-id='cart-remove-item']"
  cart_item_selector = "a[data-test-id='cart-item-link']"
  empty_cart_selector = "div[class='empty-cart']"
  btn_cart_checkout_selector = "button[data-test-id='cta-top']"

  def RemoveProductFromCart(self, productName):
    cart = self.driver.find_element(By.CSS_SELECTOR, self.cart_icon_selector)
    cart.click()
    btn_remove_from_cart = self.driver.find_element(By.CSS_SELECTOR, self.btn_remove_from_cart_selector)
    btn_remove_from_cart.click()

  def VerifyProductIsPresentInCart(self, productLink):
    cart = self.driver.find_element(By.CSS_SELECTOR, self.cart_icon_selector)
    cart.click()
    cart_items = self.driver.find_elements(By.CSS_SELECTOR, self.cart_item_selector)
    for cart_item in cart_items:
      if productLink in cart_item.get_attribute("href"):
         return 
    assert False, "product not found in cart"
    #self.wait.until(self.EC.text_to_be_present_in_element((By.CSS_SELECTOR, self.section_cart_selector), productName)) - alternative check
  
  def CheckoutCart(self):
    btn_cart_checkout = self.driver.find_element(By.CSS_SELECTOR, self.btn_cart_checkout_selector)
    btn_cart_checkout.click()    

  def VerifyCartIsEmpty(self):
    self.wait.until(self.EC.text_to_be_present_in_element((By.CSS_SELECTOR, self.empty_cart_selector), "You don't have any items in your cart."))

