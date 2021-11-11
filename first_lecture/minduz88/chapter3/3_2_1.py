from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://m.pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")

ulListRankList = bsObj.find('ul', {'class':'list rank-list'})

liList = ulListRankList.findAll('li')

list = [1,2,3,4]
for li in liList:
    liTit = li.find('span', {'class': 'tit'})
    print(liTit.text)
