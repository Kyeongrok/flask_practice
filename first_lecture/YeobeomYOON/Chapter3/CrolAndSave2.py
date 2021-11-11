from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pann.nate.com/talk/c20003")
bsObj = BeautifulSoup(html, "html.parser")

# print(bsObj)

trList = bsObj.find('table', {'class':'talk_list'}).find('tbody').findAll('tr')

# print(trList)

for tr in trList:

    trA = tr.find('a')

    # print(trA)

    print(trA.text)

f = open("새파일3.txt", 'w', encoding='utf-8')
f.write(str(trA))