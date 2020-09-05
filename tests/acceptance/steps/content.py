from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title.is_displayed()
    # checks that the user can see the tag, e.g. if display is NONE in HTML, this would return false

@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    assert page.title.text == content
    # checks that the title tag is equal to the content coming in from the step

# if you want to use the step in multiple places, e.g. a given and a then, you can just use @step
# By.CSS_SELECTOR is also a really powerful way to find elements
# the most powerful but most complex is by XPATH

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.browser)

    assert page.posts_section.is_displayed()

@then('I can see there is a post with title "Test Post" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.brower)
    posts_with_title = [post for post in page.posts if post.text == title]
    # will give us all the posts in the page
    # post is a selenium element which gives us the content of the DOM element, which should be the post title

    assert len(posts_with_title) > 0
    # assert all([post.is_displayed() for post in posts_with_title])

    # a Python trick which evaluates to true if all elements are true, or false if any are not true
    # 'any' evaluates to true if any are true, or false if all are false
    # but we want at least one post with the title we passed in