from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://news.naver.com/")
bsObj = BeautifulSoup(html, "html.parser")

wikiRefer = bsObj.findAll("a", href=re.compile("http:\/\/news.naver.com.*"))
for link in wikiRefer:
    print(link.attrs['href'])

