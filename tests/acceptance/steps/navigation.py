from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')
# allows our steps to receive arguments from the scenarios



@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    # launches a new Chrome window via the PATH and gives you access programmatically
    # always necessary for the first step (i.e. @given)
    # chromedriver is saved in /usr/local/bin
    # needs to be updated if Chrome is updated so the versions are the same
    # using context ensures that subsequent steps will have the updated context
    page = HomePage(context.browser)
    context.browser.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = BlogPage(context.browser)
    context.browser.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = NewPostPage(context.browser)
    context.browser.get(page.url)

@then('I am on the blog page')
# we can use the same function name as the decorators are not telling Python to keep the function name
# functions will be renamed by the decorator
# you won't be searching your code by function name, you'll be relying on the step names in the feature file
def step_impl(context):
    expected_url = BlogPage(context.browser).url
    assert context.browser.current_url == expected_url
    # these are standard Python asserts
    # passes because the URL will have changed even if the page has not finished loading (see @when in interactions)

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.browser).url
    assert context.browser.current_url == expected_url
