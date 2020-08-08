import requests
import argparse
from threading import Thread


argss =  argparse.ArgumentParser(description='How to use this script....')
argss.add_argument('-u', '--url', type=str, help='Enter the url after -u ...,')
parser = argss.parse_args()

methods = ['Get', 'PUT', 'Post', 'Head', 'Trace', 'Patch', 'Delete', 'Connect', 'Options']


print '===================== TESTING METHODS ======================'

def look(method):
	try:
		data = requests.request(method, parser.url)
		print 'Method ',method,' : ','Code ',data.status_code
	except:
		pass

for method in methods:
	look(method)
print '===================== TESTING END ========================='
