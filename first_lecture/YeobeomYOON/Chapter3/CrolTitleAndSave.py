from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://search.r114.co.kr/sell.aspx?keyword=%B0%FC%BE%C7%B1%B8%20%BF%C0%C7%C7%BD%BA%C5%DA&re=&lastkeyword=%B0%FC%BE%C7%B1%B8%20%BF%C0%C7%C7%BD%BA%C5%DA@")
bsObj = BeautifulSoup(html, "html.parser")

# ulItem = bsObj.find('ul', {'class':'list rank-list'})
# liList = ulItem.findAll('li')
# for li in liList:
#     liTit = li.find("span", {"class":'tit'})
#
# f = open("새파일.txt", 'w', encoding='utf-8')
# f.write(str(liTit.text))

ulItem = bsObj.find('tr', {'class':'st1'})
tdList = ulItem.findAll('td')
for td in tdList:
    tdTit = td.find('a', {"class":"blue in view_link"})
    try:
        print(tdTit)
    except:
        pass
    # print(liTit)

# print(liList)

# f = open("새파일2.txt", 'w', encoding='utf-8')
# f.write(str(liTit))