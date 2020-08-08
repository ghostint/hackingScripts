from requests import get
from bs4 import BeautifulSoup
from sys import argv, exit



#   ================================================
# 
# Will scarp <img>, <form> , <script>, <style> tags.
#
#   ================================================


def Scrape(data, tag, attrb):
    soup = BeautifulSoup(data, "lxml")
    tags = soup.findAll(str(tag))
    if tags:
        print("\n============== {} ============".format(tag))
        for tag in tags:
            try:
                if tag[attrb]:
                    print(tag[attrb])
            except:
                pass
        print("==============================")

def main():
    tags = {"iframe":"src","script":"src", "form":"action", "link":"href", "img":"src"}

    req = get(str(argv[1]))
    data = req.text

    for tag in tags.keys():
        Scrape(data, tag, tags[tag])

if __name__ == "__main__":
    main()







