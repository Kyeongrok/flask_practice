from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html, "html.parser")

# print(bs0bj)

nameList = bs0bj.findAll("span", {"class":"green"})

# for name in nameList:
print(nameList)
    # print(name.get_text())

# Tag란 <>로 시작해서 </>로 끝나는 것