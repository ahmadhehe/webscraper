import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
url = 'https://www.foodpanda.pk/restaurants/new?lat=24.82810582800003&lng=67.02127301400003&vertical=restaurants'
source_code = requests.get(url, headers=headers)
text = source_code.text
soup = BeautifulSoup(text, "html.parser")
print(soup)
