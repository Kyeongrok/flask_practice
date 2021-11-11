from urllib.request import urlopen
from bs4 import BeautifulSoup

# 네이트판 모바일 30대 제목 추출
html = urlopen("http://m.pann.nate.com/talk/c20003")
bsObj = BeautifulSoup(html, "html.parser")

urLlistRankList = bsObj.find("div", {'class':'list-wrap talk'})
liList = urLlistRankList.find("ul",  {'class':'list rank-list'}).findAll("li")

f = open("natepann.txt", 'w', encoding='utf-8')

for li in liList :
    spanliList = li.find("span", {'class': 'tit'})
    f.write(str(spanliList.text) + "\n")
