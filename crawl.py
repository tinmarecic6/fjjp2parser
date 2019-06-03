import requests
from bs4 import BeautifulSoup
import time


def get_links(url):
    
    r = requests.get(url)
    source = r.text.encode(r.encoding)
    soup = BeautifulSoup(source, "lxml")

    source = ""
    for paragraph in soup.find_all('p'):
        source += str(paragraph.encode('UTF-8'))
    soup2 = BeautifulSoup(source, 'lxml')
    
    links = []
    for link in soup2.find_all('a'):
        if link.get('href') and link.get('title'):
            if link.get('href') not in links and link.get('href')[:6] == "/wiki/":
                links.append( link.get('href') )
    
    return links


def get_introtext(url):
    
    r = requests.get(url)
    source = r.text.encode(r.encoding)
    soup = BeautifulSoup(source, "lxml")
    
    intro_text = soup.find_all('p')[0].get_text()
    i = 0
    while len(intro_text) < 100 and soup.find_all('p')[i]:
        i += 1
        intro_text += soup.find_all('p')[i].get_text()
        
    return intro_text.strip()


domain = "https://en.wikipedia.org"
wiki = "/wiki/Experiment"
url = domain + wiki

fw = open("root-" + wiki.split("/")[-1] + ".txt", "w")
fw.write(get_introtext(url))
fw.close()

for link in get_links(url):
    
    time.sleep(1)
    print("\n" + link)
    name = link.split("/")[-1] + ".txt"
    intro_text = get_introtext(domain+link)
    print(intro_text)
    fw = open(name, "w")
    fw.write(intro_text)
    fw.close()
    
    fa = open(name, "a")
    fa.write("\n\n")
    for link2 in get_links(domain+link):
        fa.write(link2 + "\n")
    fa.close()
