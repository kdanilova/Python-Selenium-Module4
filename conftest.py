import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    #add browser-name option
    parser.addoption('--browser_name', action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    ##add language option
    parser.addoption('--language', action="store", default="en",
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    #get option from command line or use default one
    browser_name = request.config.getoption("browser_name")
    #get option from command line
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
