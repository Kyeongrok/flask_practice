from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

# 김민규

nameList = bsObj.findAll("span", {"class":"green"})

print(nameList)

