from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random as rand

#i could've just gotten the makeshift link for the random article, but that was boring..

i = 0
def randomwiki(url,i):
    i +=1
    if i <= 10:
        req = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
        content = urlopen(req, timeout=10).read()
        page = BeautifulSoup(content,'html.parser')

        linksparent = page.find('body').find_all('a')

        b_links = [l.attrs.get('href') for l in linksparent]
        dowant = ['/wiki/']
        b_links_new = [f'https://en.wikipedia.org{b}' for b in b_links if b!= None and all(b.startswith(d) for d in dowant)
            and ':' not in b and 'Main_Page' not in b and '#' not in b]
        rand.shuffle(b_links_new)
        linktoscrape = 0
        for n in b_links_new:
            linktoscrape = n
            break
        print(linktoscrape)
        randomwiki(linktoscrape, i)

randomwiki('https://en.wikipedia.org/wiki/potato', i)
