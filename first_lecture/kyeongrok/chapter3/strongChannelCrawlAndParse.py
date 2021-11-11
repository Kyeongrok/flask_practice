from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://m.pann.nate.com/talk/c20038")
bsObj = BeautifulSoup(html, "html.parser")

ulItem = bsObj.find('ul', {'class':'list rank-list'})

f = open("새파일.txt", 'w', encoding='utf-8')
liList = ulItem.findAll('li')
for li in liList:
    spanTit = li.find('strong')

    try:
        print(spanTit.text)
    except:
        pass
    # f.write(str(spanTit.text) + "\n")

