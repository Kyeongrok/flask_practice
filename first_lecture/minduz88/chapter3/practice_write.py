from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://m.pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")

ulListRankList = bsObj.find('ul', {'class':'list rank-list'})

liList = ulListRankList.findAll('li')

f = open("새파일.txt", 'w', encoding='utf-8')

for li in liList :
    liTit = li.find('span', {'class':'tit'})
    liTitStrong = liTit.find('strong', {'class': 'channel'})
    try:
        f.write(str(liTitStrong.text)+ "\n")
    except:
        pass
