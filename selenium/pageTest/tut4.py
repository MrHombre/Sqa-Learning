import unittest
from selenium import webdriver
import page

chrome_path = r"D:\chromedriver\chromedriver.exe"

class AmiamiComSearch(unittest.TestCase):
    """A sample test class to showw how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.get("http://amiami.com")

    def test_search_in_amiami_com(self):
        """
        Tests amiami.com search feature. Searches for the word "gundam" then verified that some results show up.
        This doesn't look for any particular text in search results. This test verifies that the results were not empty.
        """

        #Load the main page. In this case the home page of Amiami.com
        main_page = page.MainPage(self.driver)

        #Sets the text of search textbox to "gundam"
        main_page.s_keywords_element = "gundam"
        main_page.click_search_btn()
        search_resutls_page = page.SearchResutlsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_resutls_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
