from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://m.pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")

f = open("새파일.txt", 'w', encoding='utf-8')

liList = bsObj.find("ul", {'class':'list rank-list'}).findAll('li')

for li in liList:
    liTit = li.find('span', {'class': 'tit'})
    print(liTit.text)


for li in liList:
    liTit = li.find('span', {'class': 'tit'})
    f.write(str(liTit.text) + "\n")

print('파일 저장이 완료 되었습니다.')
