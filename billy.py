from urllib import request
from bs4 import BeautifulSoup

def checkLink(host, url):
    if(not url.startswith('http')):
        url = host + url
    print(url)
    try:
        req = request.urlopen(url)
        
        html = BeautifulSoup(req, "html.parser")
        links = html.findAll('a')
        print(html.find('title'))
        for link in links:
            checkLink(host, link['href'])
        links = html.findAll('img')
        for link in links:
            checkLink(host, link['src'])        
    except:
        faulty_links.append(url)
        
    

ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

faulty_links = []

checkLink('https://commentvendresamaison.fr/', '')
        
print(faulty_links)