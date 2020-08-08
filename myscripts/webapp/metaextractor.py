import requests
from bs4 import BeautifulSoup as bs
import sys

print("===============================================================")
print("Scraped with metascraper......\n")
url = str(sys.argv[1])
print("Url is {0}".format(url))
print("===============================================================")
req = requests.get(url)
data = req.text
soup = bs(data, "lxml")
head = soup.head
metas = head.findAll("meta")

for meta in metas:
    keys = meta.attrs.keys()
    for key in keys:
        print(key," : ",meta.attrs[key],"\n")

print("================================================================")

