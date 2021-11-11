
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://search.r114.co.kr/sell.aspx?keyword=%B0%FC%BE%C7%B1%B8%20%BF%C0%C7%C7%BD%BA%C5%DA&re=&lastkeyword=%B0%FC%BE%C7%B1%B8%20%BF%C0%C7%C7%BD%BA%C5%DA@")
bsObj = BeautifulSoup(html, "html.parser", from_encoding='euc-kr')

listCellAl = bsObj.findAll('td', {'class':'list_cell al'})

for item in listCellAl:
    span = item.find('span', {'class':'list_cell_underline'})

    try:
        print(span.text)
    except:
        pass
