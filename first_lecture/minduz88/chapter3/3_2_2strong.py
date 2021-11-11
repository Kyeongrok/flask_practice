from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://m.pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")

ulListRankList = bsObj.find('ul', {'class':'list rank-list'})

liList = ulListRankList.findAll('li')
f = open("새파일.txt", 'w', encoding='utf-8')
list = [1,2,3,4]
for li in liList:
    liTit = li.find('span', {'class': 'tit'})
    liTitStrong = liTit.find('strong', {'class':'channel'})
    f.write(str(liTitStrong))
# f = open("새파일.txt", 'w', encoding='utf-8')
#     # for a in liTitStrong :
#     #     print(a.text)
# ulItem = bsObj.find('ul', {'class':'list rank-list'})
# liList = ulItem.findAll('li')
# for liL in liList :
#     lilTit = li.find('span', {'class':'tit'})
#     lilTintStrong = lilTit.find('strong', {'class':'channel'})
#     f.write(str(lilTintStrong))
# # 새파일.txt로 파일로 저장하기

