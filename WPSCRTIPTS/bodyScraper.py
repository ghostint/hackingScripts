import requests
import argparse
from bs4 import BeautifulSoup
from termcolor import colored


parser = argparse.ArgumentParser(description="A simple script to scrap the head of a  website.\nHow to use:\n\tpython wpHeadScraper.py -u https://www.webiste.com -t meta.\nUse tags like: meta, link etc." )
parser.add_argument('-u', '--url', help="Url here", type=str)
parser.add_argument('-t', '--tag', help="Tag to scrap", type=str)
args = parser.parse_args()

header = {"User-agent":"Mozzila/5.0"}

def main():
	req = requests.get(args.url, headers=header)
	soup = BeautifulSoup(req.text, 'lxml')
	body = soup.body

	tags = body.find_all(args.tag)
	print colored("|======== PREDATA ======|", color="green")
	print colored("|Items founded "+str(len(tags))+"\t|", color="green")
	print colored("|======== PREDATA ======|", color="green")

	print "========================================================"*2
	for t in tags:
		print colored(t,color="cyan")
		print ''
	print "========================================================"*2

main()

