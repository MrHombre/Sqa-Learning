from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = r"D:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get("http://amiami.com")
elem = driver.find_element_by_name("s_keywords")
elem.send_keys("gundam")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.find_element_by_xpath("""//*[@id="search_table"]/table/tbody/tr[1]/td[1]""").click()

posts = driver.find_elements_by_class_name("product_name_list")

for post in posts:
    print(post.text)
