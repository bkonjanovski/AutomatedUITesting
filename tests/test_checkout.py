import unittest
from selenium import webdriver
from pages.ItemsPage import ItemsPage
from pages.ProductPage import ProductPage
from pages.CheckoutPage import CheckoutPage

class EcommerceTests(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.maximize_window()

  def test_checkout_E2E(self):
    driver = self.driver
    driver.get("https://www.ebay.com/globaldeals")
        
    itemsPage = ItemsPage(driver)
    itemsPage.SelectRandomItem()

    productPage = ProductPage(driver)
    productPage.ChooseProductOptions()
    productPage.BuyProductasGuest()
        
    checkoutPage = CheckoutPage(driver)
    checkoutPage.EnterRandomCustomerInformation()
    checkoutPage.EnterRandomPaymentInformation()
    checkoutPage.ConfirmOrder()
        
  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    

