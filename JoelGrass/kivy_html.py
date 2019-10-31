from bs4 import BeautifulSoup
import requests
html = requests.get('https://kivy.org/doc/stable/api-kivy.html').text
soup = BeautifulSoup(html,'html5lib')


tags= [a for a in soup('a')
      if 'api-kivy' in a.get('href').split('.')[0]
       and ['reference', 'internal'] == a.get('class',[])]
api = dict()
for tag in tags:
    api[tag.get('href').split('.',maxsplit=1)[1].replace('.html','')] = tag.text
print(api)