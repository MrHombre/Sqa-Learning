from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    search_btn = (By.XPATH, '//*[@id="header"]/div[2]/form/input[2]')

class SearchResutlsPageLocators(object):
    """A class for search results locators. All search results should come here"""
    pass
