import requests
from bs4 import BeautifulSoup
import sys

url = str(sys.argv[1])
br = requests.get(url, headers={'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'})
data = br.text
soup = BeautifulSoup(data, 'lxml')
links = soup.find_all('a')
paths = soup.find_all('img')
paths += soup.find_all('script')
print '====================== LINKS FOUNDED ===========================\n'
for link in links:
    try:
    	l = str(link['href'])
    	if l.startswith('#'):
        	pass
    	else:
        	print l
    except:
	  print 'Error'
print '====================== END ======================================'

print '\n=================== Directoires Found =========================\n'
for path in paths:
	try:
		if not path['src']:
			pass
		else:
			p = str(path['src'])
			print  p
	except Exception as e:
		pass

print '==================== END ========================================='

		
