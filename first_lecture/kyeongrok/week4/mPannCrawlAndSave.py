from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://m.pann.nate.com/talk/c20003")
bsObj = BeautifulSoup(html, "html.parser")

liList = bsObj.find("div", {'class':'list-wrap talk'}).find("ul", {'class':'list rank-list'}).findAll("li")

for li in liList:
    liTit = li.find("span", {'class':'tit'})
    print(liTit.text)



