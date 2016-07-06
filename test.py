import requests
from bs4 import BeautifulSoup

song_name = 'Beautiful Day'
song_url = song_name.lower().replace(" ", "-")

url = 'http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}'.format(song_name)

content = requests.get(url).text
souper = BeautifulSoup(content,'html.parser')
results = souper.find_all('a', class_='ryzh22')

for result in results:
    hostname = 'http://www.guitartabs.cc/'
    song_url = hostname + result.attrs['href']
    content = requests.get(song_url).text
    souper = BeautifulSoup(content, 'html.parser')
    result = souper.find('div', class_='tabcont')
    print(result.text)
