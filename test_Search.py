# Implement a test case

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from SearchPageObjects import SearchPage

class TestIMDbSearchPage:

    @pytest.fixture(scope="class")
    # The setup method is a fixture that initializes the WebDriver instance with specific options,
    # maximizes the window, and quits the browser after the test is completed.
    def setup(self):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    # The test_search_page method is the actual test case that navigates to IMDb search page,
    # fills in various search fields, and clicks on different buttons to test IMDb search functionality
    def test_search_page(self, setup):
        driver = setup

        # WebDriverWait to wait for certain conditions (like element visibility, presence) before
        # interacting with the elements on the page
        wait = WebDriverWait(driver, 20)

        # Open the URL
        driver.get("https://www.imdb.com/search/name/")

        # When we are creating an object of the class, constructor will automatically invoked.
        search_page=SearchPage(driver)

        # Passing the values for all inputs
        search_page.disableExpandBtn()
        search_page.setNameInput("Brendan Fraser")
        search_page.setBirthDate("admin")
        search_page.setBirthDay("admin")
        search_page.setAwardsBtn()
        search_page.setPageBtn()
        search_page.setBirthPlaceSelect()
        search_page.setBirthPlaceOption()
        search_page.setGenderBtn()
        search_page.clickSearch()
        print(driver.title)

        # The test asserts if the title of the page contains "Name Matching" which indicates that the search was successful
        assert "Name Matching" in driver.title

        # After executing the test, it prints "Successful..." to indicate the successful execution of the test case
        print("Successful...")

# Command for running test_search in terminal
# python -m pytest -v -s TASKS\TASK-26\test_Search.py