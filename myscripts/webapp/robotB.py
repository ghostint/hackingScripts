import requests
import sys
import re

def ParseRobot(data):
	regex1 = re.compile(r'/\w*/\w*/\w*')
	regex2 = re.compile(r'/\w*/?')
	print(regex2.findall(data))
	print("")
	print(regex1.findall(data))


url = str(sys.argv[1])
uri = '/robots.txt'

url += uri

req = requests.get(url, headers={'User-agnet':'Mozzila/5.0'})

ParseRobot(req.text)