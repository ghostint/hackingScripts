import requests
import sys

url = str(sys.argv[1])
userAgent = {"User-agent": "Mozzila/5.0"}

if not url.endswith('/wp-includes/'):
	url += '/wp-inclues/'
else:
	url = url


path = 'dirs.txt'
f = open(path, 'r')
data = f.readlines()

print("\n|============================================================|")
print("|{0}|\t\t\t\t|{1}|".format("Status Code", "Url"))
print("|============================================================|")

for link in data:
	try:
		link = link.split('\n')[0]
		req = requests.get(url+link, headers=userAgent)
		print("{0}\t\t\t{1}".format(req.status_code, url+link))
	except requests.Exception as e:
		pass


f.close()