from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://news.naver.com/")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])