import requests
import argparse
from bs4 import BeautifulSoup
from termcolor import colored


parser = argparse.ArgumentParser(description="A simple script to scrap the head of a  website.\nHow to use:\n\tpython wpHeadScraper.py -u https://www.webiste.com -t meta.\nUse tags like: meta, link etc." )
parser.add_argument('-u', '--url', help="Url here", type=str)
parser.add_argument('-t', '--tag', help="Tag to scrap", type=str)
args = parser.parse_args()

headers = {'User-agent':'Mozzila/5.0'}

def main():
	req = requests.get(args.url, headers = headers)
	soup = BeautifulSoup(req.text, 'lxml')

	tags = soup.head.find_all(args.tag)

	for tag in tags:
		print colored(str(tag), color='cyan')
	
main()





