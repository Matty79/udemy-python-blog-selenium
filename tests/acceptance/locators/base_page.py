from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'  # this is a tuple without the brackets, as the comma tells Python that's what it is
    NAV_LINKS = By.CLASS_NAME, 'nav-link'  # if we want to do something more targeted, we can search by.ID
