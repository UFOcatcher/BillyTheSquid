from urllib import request
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

host = 'https://www.pagesjaunes.fr'

faulty_links = []

find404('http://harvest-moon-france.pagesperso-orange.fr/ds/')

print(faulty_links)

def find404(url):
    #test link
    
    #if not 404
    #list links on page
    #foreach link
    #test link



next_page_link = host + '/annuaire/chercherlespros?quoiqui=' + secteur + '&ou=toulouse&proximite=0&page=' + str(page)
while (not stop):
    req = request.Request(next_page_link)
    req.add_header('User-Agent', ua)
    html = BeautifulSoup(request.urlopen(req), "html.parser")
    
    if(html.find('h1') is None):
        stop = True
    else:
        #list links
        links = html.findAll('a', 'denomination-links')
        for link in links:
            if (link['href'] != '') & (link['href'] != '#'):
                company_links.append(link['href'])
        
        #go to next results page if possible
        if html.find('a', 'next') is not None:
            if (html.find('a', 'next')['href'] != '#'):
                next_page_link = host + html.find('a', 'next')['href']
        else:
            next_page_link = ''
            
        page = page + 1
        
        next_page_link = host + '/annuaire/chercherlespros?quoiqui=' + secteur + '&ou=toulouse&proximite=0&page=' + str(page)
    
for company_link in company_links:
    req = request.Request(host + company_link)
    req.add_header('User-Agent', ua)
    html = BeautifulSoup(request.urlopen(req), "html.parser")
    
    company = Company()
    
    #siret
    if (html.find('span', 'valeur') is not None):
        company.siret = html.find('span', 'valeur').string.strip()
    else:
        company.siret = ''
    
    #name
    if (html.find('h1') is not None) & (html.find('h1').string is not None):
        company.name = html.find('h1').string.strip()
    else:
        company.name = ''
    
    #phone
    if (html.find('span', 'coord-numero-mobile') is not None):
        company.phone = html.find('span', 'coord-numero-mobile')['content'].strip()
    else:
        company.phone = ''
    
    #website
    if (html.find('a', 'STANDARD') is not None):
        if (html.find('a', 'STANDARD')['href'] != '#'):
            company.website = html.find('a', 'STANDARD')['href'].strip()
        else:
            company.website = ''
    else:
        company.website = ''
    
    #manager
    
    print(company)
    
    companies.append(company)