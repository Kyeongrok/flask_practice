from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pann.nate.com/")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("a")
print(nameList)
print(len(nameList))

