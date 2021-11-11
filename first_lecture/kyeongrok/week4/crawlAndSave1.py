from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://m.pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")

ulListRankList = bsObj.find('ul', {'class':'list rank-list'})
liList = ulListRankList.findAll('li')

file = open("새파일.txt", 'w', encoding='utf-8')
for li in liList:
    liTit = li.find('span', {'class':'tit'})
    file.write(liTit.text + "\n")


