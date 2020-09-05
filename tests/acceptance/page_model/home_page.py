from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    # the home page doesn't have a title property until we make it inherit from BasePage
    # this also allows us to remove the init method as it's already present in BasePage

    # we can define the following methods as properties because they don't take any arguments
    # this allows us to access it without the brackets in our tests as if it were a property of the object
    @property
    def url(self):
        return super(HomePage, self).url + '/'
    # this allows us to access the URL via the HomePage super class of BasePage
    # so if we change domains, we only have to change the BasePage, not the URL everywhere in our tests

    # @property
    # def title(self):
    #     return self.driver.find_element(*HomePageLocators.TITLE)
    # this code removed after we inherit the title from BasePage

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)