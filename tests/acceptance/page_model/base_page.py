# will contain only those things that are shared between all pages
# if we decide the not all pages will have a title, for example, then we can remove that from the BasePage

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    # driver is the same as browser, i.e. chrome webdriver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)
    # we must pass 2 arguments - the way of searching and the search argument - see the locators file
    # we add the asterisk to deconstruct the tuple and pass it as 2 individual arguments
    # we would need to search by ID if we had multiple h1 occurrences

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)
    # returns a list of the elements