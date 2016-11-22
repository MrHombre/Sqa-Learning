import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = r"D:\chromedriver\chromedriver.exe"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(chrome_path)

    def test_search_in_python(self):
        driver = self.driver
        driver.get("http://amiami.com")
        elem = driver.find_element_by_name("s_keywords")
        elem.send_keys("gundam")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


# Future goals is to take search resutls and fine tune to show certain iteams printed out and prices. Like webscraping but in a test format.
