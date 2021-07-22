import requests
from bs4 import BeautifulSoup
import csv

x = ""
z = ""
def singleitem(item_url):
    sourcecode = requests.get(item_url)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext, 'html.parser')
    for price in soup.findAll('span', {'itemprop': 'price'}):
        global z
        z = price.string
    for itemname in soup.findAll('span', {'class':'description'}):
        #print (itemname.string)
        global x
        x = itemname.text
        print(x)
        #print(x)
        #for x in soup.findAll('div'):
            #print (x)

def trade_spider():
    page = 1
    if page == 1:
        url = "https://www.webstaurantstore.com/25887/commercial-gas-ranges.html?page=" + str(page)
        sourcecode = requests.get(url)
        plaintext = sourcecode.text
        soup = BeautifulSoup(plaintext, 'html.parser')
        file = open('mycsv.csv', 'w')
        writer = csv.writer(file)
        writer.writerow(['name', 'url', 'code', 'price'])

        for link in soup.find_all('a', {"class": 'description'}):

            href = "https://www.webstaurantstore.com" + link.get('href')
            href1 = href.strip().strip('b')
            title = link.string.strip()

            #writer.writerow([title.decode('utf-8'), href1.decode('utf-8')])
            writer.writerow([title, href1, x, z])




            #print (title)
            singleitem(href)
            #print(href)




singleitem("https://www.webstaurantstore.com/vendors.html")
