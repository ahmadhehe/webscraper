import requests
from bs4 import BeautifulSoup
import csv

def trade_spider(maxpages):
    page = 1
    while page <= maxpages:
        url = "https://www.webstaurantstore.com/25887/commercial-gas-ranges.html?page=" + str(page)
        sourcecode = requests.get(url)
        plaintext = sourcecode.text
        soup = BeautifulSoup(plaintext, 'html.parser')
        file = open('mycsv.csv', 'w')
        writer = csv.writer(file)
        writer.writerow(['name', 'url'])
        for link in soup.findAll('a', {"data-testid": 'itemDescription'}):
            itemlink = "http://www.webstaurantstore.com" + link.get('href')
            title = link.string
            writer.writerow([title, itemlink])
        page+=1

trade_spider(3)
