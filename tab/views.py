import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def song_search_view(request):
    song_name = request.GET.get('song_name') or 'happy'
    song_url = 'http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}'.format(song_name)
    content = requests.get(song_url).text
    souper = BeautifulSoup(content,'html.parser')
    results = souper.find_all('a', class_='ryzh22')
    links = [link['href'] for link in results]
    pagination = souper.find_all('div', class_='paging')
    return render(request, 'index.html', {"links":links, 'pagination':pagination})

def tab_detail_view(request, url):
    tab_url = 'http://www.guitartabs.cc/' + url
    tab_result = requests.get(tab_url).text
    souper = BeautifulSoup(tab_result, 'html.parser')
    tabs = str(souper.find('div', class_='tabcont'))
    return render(request, 'detail.html', {'tabs':tabs})
