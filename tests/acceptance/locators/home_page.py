# locators describe how we search for each element and what the element is going to be
# e.g. could be by tag name, ID or classname

from selenium.webdriver.common.by import By


class HomePageLocators:
    NAVIGATION_LINK = By.ID, 'blog-link'

    # having these mean we no longer have to change them everywhere in our tests, we can just change them here
