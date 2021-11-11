from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

f = open("새파일.txt", 'w', encoding='utf-8')

aList = bsObj.findAll("a")

for link in aList:
    if 'href' in link.attrs:
        print(link.attrs['href'])

for link in aList:
    if 'href' in link.attrs:
        f.write(link.attrs['href'] + "\n")

print('파일 저장이 완료 되었습니다.')
