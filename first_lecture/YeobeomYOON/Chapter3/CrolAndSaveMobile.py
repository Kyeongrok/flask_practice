from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://m.pann.nate.com/talk/c20003")
bsObj = BeautifulSoup(html, "html.parser")

liList = bsObj.find('ul', {'class':'list rank-list'}).findAll('li')

# print(liList)

f = open("새파일4.txt", 'w', encoding='utf-8')

for li in liList:
    # print(li)
    liTit = li.find("span", {'class':'tit'})
    print(liTit.text)
    f.write(str(liTit.text + "\n"))

