import bs4
import requests

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newOfferAccordionRow .header-price')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/PlayStation-4-Slim-1TB-Console/dp/B071CV8CG2/ref=sr_1_1?s=videogames&ie=UTF8&qid=1523661604&sr=1-1&keywords=playstation%2B4&dpID=31qwualUaLL&preST=_SX300_QL70_&dpSrc=srch&th=1')
print('The price is ' + price)
