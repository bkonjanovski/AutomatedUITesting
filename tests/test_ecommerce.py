import unittest
from selenium import webdriver
from pages.ItemsPage import ItemsPage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage
from pages.SigninPage import SigninPage
from pages.CheckoutPage import CheckoutPage

class EcommerceTests(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()
    self.base_url = "https://www.ebay.com/globaldeals/home/toys/"
    self.driver.get(self.base_url)

  #POSITIVE SCENARIOS (happy-path)
  def test_add_product_to_cart(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productLink = productPage.AddProductToCart()        
    cartPage = CartPage(self.driver)
    cartPage.VerifyProductIsPresentInCart(productLink)

  def test_remove_product_from_cart(self):
    itemsPage = ItemsPage(self.driver)
    productName = itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productLink = productPage.AddProductToCart()        
    cartPage = CartPage(self.driver)
    cartPage.VerifyProductIsPresentInCart(productLink)
    cartPage.RemoveProductFromCart(productName)
    cartPage.VerifyCartIsEmpty()   

  def test_add_multiple_products_to_cart(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productLink_1 = productPage.AddProductToCart()        
    cartPage = CartPage(self.driver)
    self.driver.get(self.base_url)
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productLink_2 = productPage.AddProductToCart()        
    cartPage = CartPage(self.driver)
    self.driver.get(self.base_url)
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productLink_3 = productPage.AddProductToCart()        
    cartPage = CartPage(self.driver)
    cartPage.VerifyProductIsPresentInCart(productLink_1)
    cartPage.VerifyProductIsPresentInCart(productLink_2)
    cartPage.VerifyProductIsPresentInCart(productLink_3)

  def test_guest_checkout_E2E(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productPage.BuyProductasGuest()
    checkoutPage = CheckoutPage(self.driver)
    checkoutPage.EnterRandomCustomerInformation()
    checkoutPage.EnterCCaymentInformation()
    checkoutPage.ConfirmOrder()

  def test_guest_checkout_payment_method_paypal(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productPage.BuyProductasGuest()
    checkoutPage = CheckoutPage(self.driver)
    checkoutPage.EnterRandomCustomerInformation()
    checkoutPage.EnterPayPalPaymentInformation()
    
        
  #NEGATIVE SCENARIOS     
  def test_invalid_login(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.OpenSignIn()
    signinPage = SigninPage(self.driver)
    signinPage.EnterInvalidLogin()
    signinPage.SubmitLogin() 
    signinPage.VerifyLoginError()

  def test_facebook_login(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.OpenSignIn()
    signinPage = SigninPage(self.driver)
    signinPage.VerifyFacebookLoginRedirection  

  def test_verify_cart_checkout_requires_login(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productLink = productPage.AddProductToCart()        
    cartPage = CartPage(self.driver)
    cartPage.VerifyProductIsPresentInCart(productLink)
    cartPage.CheckoutCart()
    SigninPage(self.driver)

  def test_verify_product_options_mandatory(self):
    self.driver.get("https://www.ebay.com/globaldeals/fashion/mens-shoes-accessories")
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.AddProductToCart()      
    productPage.VerifyErrorMessage()  

  def test_invalid_payment_details(self):
    itemsPage = ItemsPage(self.driver)
    itemsPage.SelectRandomItem()
    productPage = ProductPage(self.driver)
    productPage.ChooseProductOptionsIfApplicable()
    productPage.BuyProductasGuest()
    checkoutPage = CheckoutPage(self.driver)
    checkoutPage.EnterRandomCustomerInformation()
    checkoutPage.EnterCCaymentInformation("0000 0000 0000 0000", "0223", "0000")
    checkoutPage.VerifyPaymentError()

  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    

