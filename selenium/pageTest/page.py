from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The Locator for the search box where search string is entered
    locator = "s_keywords"

class BasePage(object):
    """Base class to init the base page the will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Home page action methods come here. I.e. Amiami.com"""

    #Declares a var that will contain the retieved text
    search_text_element = SearchTextElement()#header > div.searchbox > form > input.search_btn

    def click_search_btn(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.search_btn)
        element.click()

class SearchResutlsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Should search for this text in the specifc page
        # elemet, but for now it works
        return "No results found." not in self.driver.page_source
