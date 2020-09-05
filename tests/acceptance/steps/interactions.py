from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')
# allows our steps to receive arguments from the scenarios


# @when('I click on the link with id "(.*)"')
# # each group of the regular expression passed above is going to become its own parameter, which we call link_id
# # dot means any expression, asterisk means any number of dots so total flexibility on how we name the id
# def step_impl(context, link_id):
#     link = context.browser.find_element_by_id(link_id)
#     # this will find the element by its id
#     link.click()
#     # selenium will move the mouse and click it
# we cannot make the above into a page step as we don't know which page to load at this point as it's too generic
# so the step below allows that flexibility

@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.browser)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]
    # provides a list of objects found by selenium where the text of the link is equal to what we've passed in
    # i.e. what the user wants to click per the acceptance tests
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.browser)
    page.form_field(field_name).send_keys(content)
    # find the field by its name and send keys will type out the content key by key as if a user were typing
    # this one step covers both of the field entry criteria in the content feature file


@when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.browser)
    page.submit_button.click()
