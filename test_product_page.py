import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage



#steps taken
@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6",
                                    pytest.param("7", marks=pytest.mark.xfail),
                                    "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # initialization of Page Object, driver and url address are passed to constructor
    page.open()  # open page
    page.should_be_add_to_basket()  # check if Add to basket button is presented
    # page.should_not_be_success_message()  # check that no success message about adding product to basket
    page.product_add_to_basket()  # click on Add to basket button
    page.solve_quiz_and_get_code()  # solving quiz from alert message and getting code
    # page.should_be_success_message()  # checking that success message is appeared after adding product to basket
    page.should_be_product_name()  # product name in message is matched to product name on product page
    page.should_be_product_price()  # product price in message is matched to product price on product page
    # page.should_message_disappeared()  # message should disappear


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_not_be_success_message() # check that no success message about adding product to basket


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message() # check that no success message about adding product to basket


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_message_disappeared() # message should disappear


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # open login page
    login_page = LoginPage(browser, browser.current_url)  # initialization Login Page
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-robot-novels_25/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_message_empty_basket()








