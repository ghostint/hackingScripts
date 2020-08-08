import requests
from bs4 import BeautifulSoup

def main():

	url = 'https://web.whatsapp.com'
	
	cookies = {'wa_lang_pref':'en','wa_csrf':'MssxcTDs0cCehFCxJkuDZX'}
	
	headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
	
	data = requests.post(url, cookies=cookies, headers=headers)
	soup = BeautifulSoup(data.text, 'lxml')
	
	elements = soup.findAll('a')
	for element in elements:
		print element
		
		
main()

