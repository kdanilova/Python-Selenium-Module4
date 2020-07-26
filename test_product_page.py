from pages.product_page import ProductPage


#steps taken
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # initialization of Page Object, driver and url address are passed to constructor
    page.open()  # open page
    page.should_be_add_to_basket()  # check if Add to basket button is presented
    page.product_add_to_basket()  # click on Add to basket button
    page.solve_quiz_and_get_code()  # solving quiz from alert message and getting code
    page.should_be_product_name()  # product name in message is matched to product name on product page
    page.should_be_product_price()  # product price in message is matched to product price on product page

