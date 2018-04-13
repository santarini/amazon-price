import bs4
import requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newOfferAccordionRow .header-price')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/PlayStation-4-Slim-1TB-Console/dp/B071CV8CG2/ref=sr_1_1?s=videogames&ie=UTF8&qid=1523661604&sr=1-1&keywords=playstation+4&dpID=31qwualUaLL&preST=_SX300_QL70_&dpSrc=srch')
print('The price is ' + price)
