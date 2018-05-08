#1Python 3

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4 as bs

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

#navigate to careers webpage
driver.get('https://www.amazon.com/s/page=1&keywords=cashews')

pageHTML = driver.find_element_by_tag_name('html')
pageHTML = pageHTML.get_attribute('innerHTML')
soup = bs.BeautifulSoup(pageHTML, 'lxml')
container = soup.find("ul", {"id": "s-results-list-atf"})
i = 1
for row in container.findAll("div", {"class": "a-fixed-left-grid-inner"}):
    itemName = row.find("h2").text
    try:
        itemWholePrice = row.find("span", {"class": "sx-price-whole"}).text
        itemFractionalPrice = row.find("sup", {"class": "sx-price-fractional"}).text
    except:
        itemWholePrice = "Missing"
        itemFractionalPrice = "Missing"
        
    print(itemName)
    print(str(itemWholePrice) + "." + str(itemFractionalPrice))

driver.dispose()
