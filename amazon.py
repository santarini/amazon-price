#!Python 3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4 as bs

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

#navigate to careers webpage
driver.get('https://www.amazon.com/s/page=1&keywords=cashews')
time.sleep(1)

pageHTML = driver.find_element_by_tag_name('html')
pageHTML = pageHTML.get_attribute('innerHTML')
soup = bs.BeautifulSoup(pageHTML, 'lxml')
container = soup.find("ul", {"id": "s-results-list-atf"})

print(container)
