Feature: test that pages have the correct content
  Scenario: Blog page has a correct title
    Given I am on the blog page
    Then There is a title shown on the page
    And The title tag has content "This is the blog page"
    # we can jump straight to then as we're not interacting with the page at all
    # multiple Givens / Whens / Thens are ok but it's better to say And

  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "This is the homepage"

    # better to keep scenarios granular and specific such that they are efficient and it's easy to identify issues

  Scenario: Blog page loads the posts
    Given I am on the blog page
    And I wait for the posts to load
    Then I can see there is a posts section on the page

    # we can either tell Selenium to wait for a fixed amount of time or tell Selenium what we're waiting for
    # you can also tell Selenium not to wait longer than x seconds

  Scenario: User can create new posts
    Given I am on the new post page
    When I enter "Test Post" in the "title" field
    And I enter "Test Content" in the "content" field
    And I press the submit button
    Then I am on the blog page
    Given I wait for the posts to load
    Then I can see there is a post with title "Test Post" in the posts section

    # the above is a more contrived user journey